from django.contrib import admin
from django.urls import path , include
from djangoUser import views
from django.contrib.auth.views import LoginView
from .forms import loginForm

urlpatterns = [
    path('', views.register),
    path('login/',LoginView.as_view(template_name='login.html',authentication_form=loginForm))
]
