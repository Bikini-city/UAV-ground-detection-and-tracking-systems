from .setups import EXP_FILE,MODEL_PATH
from .YOLOX.tools.demo import main,make_parser,get_exp


def detect(src):
    # Perform Transaction
    confidence = float(0.25)
    # detections = Detections.objects.create(image_to_detect=image_to_detect,confidence=confidence)
    VAL_IMG_PATH = src
    
    # YOLOX PARAMETERS
    conf = confidence
    args = make_parser().parse_args()
    split = str(VAL_IMG_PATH).split('.')[1]
    
    if (split == "jpg" or split == 'jpeg' or split == 'png'):
        args.demo = "image"
    elif (split == "MP4"):
        args.demo = "video"
        
    args.exp_file = EXP_FILE
    args.ckpt = MODEL_PATH
    args.path = VAL_IMG_PATH
    args.conf = conf
    args.nms = 0.45
    args.tsize = 640
    args.save_result = True
    exp = get_exp(args.exp_file, args.name)

    # YOLOX DETECTOR
    print("=== args : ",args)
    jfile = main(exp,args)
    
    down = jfile["down"]
    broken = jfile["broken"]
    return down, broken