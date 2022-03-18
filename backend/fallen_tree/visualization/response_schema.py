from drf_yasg import openapi
from .serializers import *

GetDataSet_response_dict = {
    "200" : openapi.Response(
        description="Success",
        schema=DataSetSerializer,
        examples={
            "application/json": [
                {
                    "id": 1,
                    "lat": "40.4240988275343500",
                    "lng": "-86.9177794290636400",
                    "src": "/media/%EC%98%81%EC%83%81.mp4",
                    "date": "2022-02-08",
                    "broken": 2,
                    "down": 3
                },
                {
                    "id": 2,
                    "lat": "40.4240988275343500",
                    "lng": "-86.9177794290636400",
                    "src": "/media/False",
                    "date": "2022-02-08",
                    "broken": 1,
                    "down": 2
                },
                {
                    "id": 3,
                    "lat": "40.4240988275343500",
                    "lng": "-86.9177794290636400",
                    "src": "/media/False",
                    "date": "2022-02-08",
                    "broken": 3,
                    "down": 4
                }
            ]
        }
    ),
}
PostDataSet_response_dict = {
    "200" : openapi.Response(
        description="Success",
        schema=DataSetSerializer,
        examples={
            "application/json" : {
                "id": 13,
                "lat": "40.4240988275343500",
                "lng": "-86.9177794290636400",
                "src": "/media/%EC%84%9C%EB%AA%85_gtv1QSR.jpg",
                "date": "2022-02-09",
                "broken": 4,
                "down": 3
            }
        }
    )
}

GetDataSetDetail_response_dict = {
    "200" : openapi.Response(
        description="Success",
        schema=DataSetSerializer,
        examples={
            "application/json" : {
                "id": 13,
                "lat": 40.4240988275343500,
                "lng": -86.9177794290636400,
                "src": "/media/%EC%84%9C%EB%AA%85_gtv1QSR.jpg",
                "date": "2022-02-09",
                "broken": 4,
                "down": 3
            }
        }
    )
}

DeleteDataSetDetail_response_dict = {
    "204" : openapi.Response(
        description="Success(HTTP_204_NO_CONTENT)",
    )
}