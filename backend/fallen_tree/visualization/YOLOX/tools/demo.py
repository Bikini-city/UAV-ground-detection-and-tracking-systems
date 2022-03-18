#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

import argparse
import time

# from loguru import logger

import cv2
import torch
import numpy as np
from fallen_tree.settings import MEDIA_ROOT,BASE_DIR

from dotenv import load_dotenv
import os
import boto3
load_dotenv()

# from visualization.YOLOX.data.data_augment import ValTransform
from visualization.YOLOX.yolox.exp import get_exp
from visualization.YOLOX.yolox.utils import fuse_model, postprocess, vis
from visualization.YOLOX.yolox.data.data_augment import ValTransform

IMAGE_EXT = [".jpg", ".jpeg", ".webp", ".bmp", ".png"]



def make_parser():
    parser = argparse.ArgumentParser("YOLOX Demo!")
    parser.add_argument(
        "demo", default="image", help="demo type, eg. image, video and webcam"
    )
    parser.add_argument("-expn", "--experiment-name", type=str, default=None)
    parser.add_argument("-n", "--name", type=str, default=None, help="model name")

    parser.add_argument(
        "--path", default="./assets/dog.jpg", help="path to images or video"
    )
    parser.add_argument("--camid", type=int, default=0, help="webcam demo camera id")
    parser.add_argument(
        "--save_result",
        action="store_true",
        help="whether to save the inference result of image/video",
    )

    # exp file
    parser.add_argument(
        "-f",
        "--exp_file",
        default=None,
        type=str,
        help="pls input your experiment description file",
    )
    parser.add_argument("-c", "--ckpt", default=None, type=str, help="ckpt for eval")
    parser.add_argument(
        "--device",
        default="cpu",
        type=str,
        help="device to run our model, can either be cpu or gpu",
    )
    parser.add_argument("--conf", default=0.3, type=float, help="test conf")
    parser.add_argument("--nms", default=0.3, type=float, help="test nms threshold")
    parser.add_argument("--tsize", default=None, type=int, help="test img size")
    parser.add_argument(
        "--fp16",
        dest="fp16",
        default=False,
        action="store_true",
        help="Adopting mix precision evaluating.",
    )
    parser.add_argument(
        "--legacy",
        dest="legacy",
        default=False,
        action="store_true",
        help="To be compatible with older versions",
    )
    parser.add_argument(
        "--fuse",
        dest="fuse",
        default=False,
        action="store_true",
        help="Fuse conv and bn for testing.",
    )
    parser.add_argument(
        "--trt",
        dest="trt",
        default=False,
        action="store_true",
        help="Using TensorRT model for testing.",
    )
    return parser


def get_image_list(path):
    image_names = []
    for maindir, subdir, file_name_list in os.walk(path):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            ext = os.path.splitext(apath)[1]
            if ext in IMAGE_EXT:
                image_names.append(apath)
    return image_names

"""from PIL import Image
s3 = boto3.resource('s3')
def read_image_from_s3(filename):
    bucket = s3.Bucket(os.getenv('AWS_STORAGE_BUCKET_NAME'))
    object = bucket.Object(filename)
    response = object.get()
    file_stream = response['Body']
    img = Image.open(file_stream)
    return img"""

def get_image_lists(src):
    session = boto3.Session( 
         aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"), 
         aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    #Then use the session to get the resource
    s3 = boto3.client('s3')
    path = str(src)
    print("path", path)
    s3.download_file(os.getenv('AWS_STORAGE_BUCKET_NAME'), path, path)

class Predictor(object):
    def __init__(
        self,
        model,
        exp,
        cls_names= ("down","broken","normal"),
        trt_file=None,
        decoder=None,
        device="cpu",
        fp16=False,
        legacy=False,
    ):
        self.model = model
        self.cls_names = cls_names
        self.decoder = decoder
        self.num_classes = exp.num_classes
        self.confthre = exp.test_conf
        self.nmsthre = exp.nmsthre
        self.test_size = exp.test_size
        self.device = device
        self.fp16 = fp16
        self.preproc = ValTransform(legacy=legacy)
        if trt_file is not None:
            from torch2trt import TRTModule
            model_trt = TRTModule()
            model_trt.load_state_dict(torch.load(trt_file))

            x = torch.ones(1, 3, exp.test_size[0], exp.test_size[1]).cuda()
            self.model(x)
            self.model = model_trt

    def inference(self, img):
        print("=== img : ",img)
        img_info = {"id": 0}
        if isinstance(img, str):
            img_info["file_name"] = os.path.basename(img)
            img = cv2.imread(img)
            img = cv2.resize(img, dsize=(416, 416))
        else:
            img_info["file_name"] = None
        print("=== img_info : ",img_info)
        height, width = img.shape[:2]
        img_info["height"] = height
        img_info["width"] = width
        img_info["raw_img"] = img

        ratio = min(self.test_size[0] / img.shape[0], self.test_size[1] / img.shape[1])
        img_info["ratio"] = ratio

        img, _ = self.preproc(img, None, self.test_size)
        img = torch.from_numpy(img).unsqueeze(0)
        img = img.float()
        if self.device == "gpu":
            img = img.cuda()
            if self.fp16:
                img = img.half()  # to FP16

        with torch.no_grad():
            outputs = self.model(img)
            if self.decoder is not None:
                outputs = self.decoder(outputs, dtype=outputs.type())
            print("======= outputs1 : ",outputs)
            outputs = postprocess(
                outputs, self.num_classes, self.confthre,
                self.nmsthre, class_agnostic=True
            )
            # logger.info("Infer time: {:.4f}s".format(time.time() - t0))
        print("======= outputs2 : ",outputs)
        return outputs, img_info

    def visual(self, output, img_info, cls_conf=0.35, demo='image'):
        print("=== output : ",output)
        temp = {}
        ratio = img_info["ratio"]
        img = img_info["raw_img"]
        if output is None:
            return img, temp
        output = output.cpu()

        bboxes = output[:, 0:4]

        # preprocessing: resize
        bboxes /= ratio

        cls = output[:, 6]
        scores = output[:, 4] * output[:, 5]
        vis_res, json_obj = vis(img, bboxes, scores, cls, cls_conf, self.cls_names, demo)
        print("=== vis_res : ",vis_res," | json_obj : ",json_obj)
        return vis_res, json_obj


def image_demo(predictor, vis_folder, path, current_time, save_result):
    json_obj = {}
    
    real_path = os.path.join(BASE_DIR, str(path))
    get_image_lists(path)
    if os.path.isdir(real_path):
        files = get_image_list(real_path)
    else:
        files = [real_path]
    files.sort()
    for image_name in files:
        outputs, img_info = predictor.inference(image_name)
        result_image, json_obj = predictor.visual(outputs[0], img_info, predictor.confthre,'image')
        # fallen, broken 개수 반환
        
        if save_result:
            save_folder = os.path.join(
                vis_folder, time.strftime("%Y_%m_%d_%H_%M_%S", current_time)
            )
            os.makedirs(save_folder, exist_ok=True)
            save_file_name = os.path.join(save_folder, os.path.basename(image_name))
            # logger.info("Saving detection result in {}".format(save_file_name))
            cv2.imwrite(save_file_name, result_image)
        ch = cv2.waitKey(0)
        if ch == 27 or ch == ord("q") or ch == ord("Q"):
            break
    return json_obj

# 동영상, 웹캡 실행
def imageflow_demo(predictor, vis_folder, current_time, args):
    print("=== vis_folder : ",vis_folder)
    json_obj = {}
    # real_path = os.path.join(BASE_DIR, str(vis_folder))
    # get_image_lists(path)
    
    path = args.path if args.demo == "video" else args.camid
    real_path = os.path.join(BASE_DIR, str(path))
    get_image_lists(path)
    print("=== real_path : ",real_path)
    cap = cv2.VideoCapture(real_path)
    cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
    cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
    save_folder = os.path.join(
        vis_folder, time.strftime("%Y_%m_%d_%H_%M_%S", current_time)
    )
    os.makedirs(save_folder, exist_ok=True)
    if args.demo == "video":
        save_path = os.path.join(save_folder, os.path.basename(real_path))
    else:
        save_path = os.path.join(save_folder, "camera.mp4")
    print("=== save_path : ",save_path)
    while True:
        ret_val, frame = cap.read()
        if np.shape(frame) == ():
            break
        else:
            resize_frame = cv2.resize(frame, (416, 416))
        print("=== ret_val : ",ret_val)
        if ret_val:
            outputs, img_info = predictor.inference(resize_frame)
            print("=== outputs : ",outputs," | img_info : ",img_info)
            result_frame, json_obj = predictor.visual(outputs[0], img_info, predictor.confthre,'video')
            # if args.save_result:
            #     vid_writer.write(result_frame)
            ch = cv2.waitKey(1)
            if ch == 27 or ch == ord("q") or ch == ord("Q"):
                break
        else:
            break
    return json_obj


def main(exp, args):
    json_obj = {}
    if not args.experiment_name:
        args.experiment_name = exp.exp_name

    file_name = os.path.join(exp.output_dir, args.experiment_name)
    os.makedirs(file_name, exist_ok=True)

    vis_folder = None
    if args.save_result:
        vis_folder = os.path.join(file_name, "vis_res")
        os.makedirs(vis_folder, exist_ok=True)

    if args.trt:
        args.device = "gpu"

    # logger.info("Args: {}".format(args))

    if args.conf is not None:
        exp.test_conf = args.conf
    if args.nms is not None:
        exp.nmsthre = args.nms
    if args.tsize is not None:
        exp.test_size = (args.tsize, args.tsize)

    model = exp.get_model()

    if args.device == "gpu":
        model.cuda()
        if args.fp16:
            model.half()  # to FP16
    model.eval()

    if not args.trt:
        if args.ckpt is None:
            ckpt_file = os.path.join(file_name, "best_ckpt.pth")
        else:
            ckpt_file = args.ckpt
        ckpt = torch.load(ckpt_file, map_location="cpu")
        # load the model state dict
        model.load_state_dict(ckpt["model"])

    if args.fuse:
        model = fuse_model(model)

    if args.trt:
        assert not args.fuse, "TensorRT model is not support model fusing!"
        trt_file = os.path.join(file_name, "model_trt.pth")
        assert os.path.exists(
            trt_file
        ), "TensorRT model is not found!\n Run python3 tools/trt.py first!"
        model.head.decode_in_inference = False
        decoder = model.head.decode_outputs
        # logger.info("Using TensorRT to inference")
    else:
        trt_file = None
        decoder = None

    predictor = Predictor(
        model, exp, ("down","broken","normal"), trt_file, decoder,
        args.device, args.fp16, args.legacy,
    )
    current_time = time.localtime()
    if args.demo == "image":
        json_obj = image_demo(predictor, vis_folder, args.path, current_time, args.save_result)
    elif args.demo == "video" or args.demo == "webcam":
        json_obj = imageflow_demo(predictor, vis_folder, current_time, args)
    print("=== json_obj : ",json_obj)
    return json_obj


if __name__ == "__main__":
    args = make_parser().parse_args()
    exp = get_exp(args.exp_file, args.name)

    json_obj = main(exp, args)