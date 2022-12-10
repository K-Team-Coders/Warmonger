from django.urls import path

from .views import *

urlpatterns = [
    path('testdata/', testdata.as_view()),
    path('testdata2/', testdata_barchart.as_view()),
    path('testdata3/', testdata_radarchart.as_view())
]
