from http import HTTPStatus
from http.client import BAD_REQUEST
from msilib.schema import Error
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from .serializers import DataSetSerializer
from .models import DataSet, FileUpload
from .response_schema import *

from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.parsers import FormParser,MultiPartParser
from rest_framework.decorators import parser_classes
from rest_framework.views import APIView
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt

from visualization.detect_fallen import detect

import os
from fallen_tree.settings import BASE_DIR
test = False

#form-data for posting dataset's image or video
src = openapi.Parameter('src', openapi.IN_FORM, type=openapi.TYPE_FILE, required=True)
lat = openapi.Parameter('lat', openapi.IN_FORM, type=openapi.TYPE_NUMBER, format=openapi.FORMAT_DECIMAL, required=True)
lng = openapi.Parameter('lng', openapi.IN_FORM, type=openapi.TYPE_NUMBER, format=openapi.FORMAT_DECIMAL, required=True)
dat = openapi.Parameter('date', openapi.IN_FORM, type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, required=True)

#GET datas/
@swagger_auto_schema(method="get",responses=GetDataSet_response_dict)
@api_view(['GET'])
def getDataSets(request):        
    response = []

    dataSets = DataSet.objects.all()
    for dataSet in dataSets:
        dataSet_json = DataSetSerializer(dataSet).data
        dataSet_json["lat"] = float(dataSet_json["lat"])
        dataSet_json["lng"] = float(dataSet_json["lng"])
        dataSet_id = dataSet_json["id"]
        try:
            result = Result.objects.get(dataSet_id=dataSet_id)
        except Result.DoesNotExist:
            continue
        result_json = ResultSerializer(result).data
        
        dataSet_json["broken"] = result_json["broken"]
        dataSet_json["down"] = result_json["down"]
        
        response.append(dataSet_json)

    return JsonResponse(response, safe=False)

#POST /datas/uploads
@swagger_auto_schema(method="post",manual_parameters=[src,lat,lng,dat],responses=PostDataSet_response_dict)
@api_view(['POST'])
@parser_classes([MultiPartParser])
@csrf_exempt
def postDataSet(request):
    try:
        error_data = {}
        if request.method == 'POST':
            lat = request.POST['lat']
            lng = request.POST['lng']
            date = request.POST['date']
            src = request.FILES.get('src',None)
            dataSet = DataSet(
                lat=lat,
                lng=lng,
                src=src,
                date=date,
            )
            dataSet.save()
            dataSet_data = DataSetSerializer(dataSet).data

            #### For Test START ####
            if test:
                result = Result(
                    broken = 4,
                    down = 3,
                    dataSet_id = dataSet
                )
                result.save()
            #### For Test END ####
            else:
                print("src",src)
                
                down, broken = detect(dataSet.src)
                result = Result (
                    broken = broken,
                    down = down,
                    dataSet_id = dataSet
                )
                result.save()
                
            result_json = ResultSerializer(result).data
            dataSet_data["broken"] = result_json["broken"]
            dataSet_data["down"] = result_json["down"]

            print("src",dataSet.src)
            os.remove(os.path.join(BASE_DIR, str(dataSet.src)))
            return JsonResponse(dataSet_data, safe=False, status=status.HTTP_201_CREATED)
        else:
            error_data["error"] = "POST /datas에서 오류가 발생함"
            return JsonResponse(error_data, safe=False, status=HTTPStatus/BAD_REQUEST)
    
    except MultiValueDictKeyError:
        error_data["error"] = "요청이 잘못되었음 form을 확인해보세요"
        return JsonResponse(error_data, safe=False, status=HTTPStatus.BAD_REQUEST)
        


class DataSetWithID(APIView):
    
    #GET datas/{id}
    @swagger_auto_schema(responses=GetDataSetDetail_response_dict)
    def get(self, request, *args, **kwargs): 
        status = HTTPStatus.OK
        error_data = {}
        # model 가져오기
        id = kwargs.get("id")
        try:
            dataSet = DataSet.objects.get(id=id)
            result = Result.objects.get(dataSet_id=id)
            dataSet_json = DataSetSerializer(dataSet).data
            dataSet_json["lat"] = float(dataSet_json["lat"])
            dataSet_json["lng"] = float(dataSet_json["lng"])
            result_json = ResultSerializer(result).data

            #응답부분에 result의 broken, down 정보 넣기
            dataSet_json["broken"] = result_json["broken"]
            dataSet_json["down"] = result_json["down"]

        except (DataSet.DoesNotExist, Result.DoesNotExist):
            error_data["error"] = "DataSet or Result Does Not Exist"
            status = HTTPStatus.NOT_FOUND
            return JsonResponse(error_data, status=status)

        return JsonResponse(dataSet_json, safe=False)

    #DELETE datas/{id}
    @swagger_auto_schema(responses=DeleteDataSetDetail_response_dict)
    def delete(self, request, *args, **kwargs):
        error_data = {}
        try:
            id = kwargs.get("id")
            dataSet = DataSet.objects.get(id=id)
            result = Result.objects.get(dataSet_id=id)

            response = DataSetSerializer(dataSet).data
            response["lat"] = float(response["lat"])
            response["lng"] = float(response["lng"])

            dataSet.delete()
            result.delete()

            return JsonResponse(response, safe=False, status=status.HTTP_204_NO_CONTENT)
        
        except (DataSet.DoesNotExist, Result.DoesNotExist):
            error_data["error"] = "DataSet or Result Does Not Exist"
            status = HTTPStatus.NOT_FOUND
            return JsonResponse(error_data, status=status)
