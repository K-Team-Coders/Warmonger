from django.urls import path

from .views import *

urlpatterns = [
    path('addNews/', addNew.as_view()),
    path('detailNews/<int:pk>/', detailedNewsView.as_view())
]
