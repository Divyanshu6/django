from django.contrib import admin
from django.urls import path , include
from djangoUser import views

urlpatterns = [
    path('', views.register),
]
