from rest_framework import serializers
from .models import *

class DataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'

class DetectionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Detections
        fields = ('id', 'image_to_detect','confidence')

class OutputsSerializerAll(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Detections
        fields = ('id', 'image_to_detect','confidence', 'code_generated', 'json_file', 'detected_image_path','processed')