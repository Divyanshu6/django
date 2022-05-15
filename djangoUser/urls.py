from django.contrib import admin
from django.urls import path , include
from djangoUser import views
from django.contrib.auth.views import LoginView
from .forms import loginForm

urlpatterns = [
    path('', views.register),
    path('api/',views.api.as_view(),name='api'),
    path('login/',LoginView.as_view(template_name='login.html',authentication_form=loginForm),name='login'),
    path('stockList/',views.stockList,name='stockList'),
    path('stockDetails/',views.stockDetails,name='stockDetails'),
]
