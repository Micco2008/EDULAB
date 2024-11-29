from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('page', views.page),
    path('path1', views.page1)
]