from django.urls import path
from .views import *

app_name = "visualization"

urlpatterns =[
    path('uploads',postDataSet),
    path('',getDataSets),
    path('<int:id>',DataSetWithID.as_view()),
]