from django.urls import path

from .views import *

urlpatterns = [
    path('addNews/', addNew.as_view()),
    path('getAllNews/', getAllNews.as_view({'get': 'list'})),
    path('getAllTags/', getAllTags.as_view({'get': 'list'}))
]
