from django import views
from django.urls import path, include
from rest_framework import routers
from .views import *

'''
urls class used to declare add all the urls used by the classifier application.
@Author erick
'''
router = routers.DefaultRouter()
router.register(r'CustomerAnalytics', DefaultScore, basename='Scoremodel')

urlpatterns = [
    path('machinelearningtest/<str:processing_option>/<uuid:client_id_url>/',ETLData.as_view(), name = "home"),   
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_frameworkDiimo')),
]
