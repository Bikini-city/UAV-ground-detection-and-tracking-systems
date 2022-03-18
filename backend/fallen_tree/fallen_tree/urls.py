import imp
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from visualization.views import *

api_info = openapi.Info(
        title="FallenTree_Visualization_API", # 타이틀
        default_version='v1', # 버전
        description="FallenTree_Visualization API 문서", # 설명
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mjh991016@naver.com"),
        license=openapi.License(name=""),
    )
schema_view = get_schema_view(
    api_info,
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('datas/', include("visualization.urls", namespace="visualization")),
    
]
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),]