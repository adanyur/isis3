from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('acreditacions/', acreditacion_api_GP),
    path('acreditacions/<str:pk>/', acreditacion_api_PGD),
]

urlpatterns = format_suffix_patterns(urlpatterns)