from asyncio import as_completed
from django.shortcuts import redirect, render
from numpy import diff
from djangoUser.forms import registrationForm , loginForm
from django.contrib.auth.views import LoginView
from rest_framework.views import APIView
from rest_framework import authentication , permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly , IsAuthenticated
from .serializers import userSerializer
from rest_framework.response import Response
import json
from djangoUser.models import extendedUser
from rest_framework.decorators import permission_classes , authentication_classes
from djangoUser import serializers
import requests
from yahoo_fin.stock_info import *
from djangoUser.templatetags import customTag
import time
from concurrent.futures import ThreadPoolExecutor , as_completed
# Create your views here.
# def register(request):
#     form=registrationForm()
#     if request.method=='GET':
#         return render(request,'register.html',{'form':form})
#     else:
#         form_data=registrationForm(data=request.POST)
#         print(form_data.errors)
#         if form_data.is_valid():
#             form_data.save()
#             return redirect('login')
#         else:
#             print("we are here")
#             for i in form_data.errors:
#                 print(i)
#             return render(request,'register.html',{'form':form,'form_data':form_data})

def register(request):
    form=registrationForm()
    return render(request,'register.html',{'form':form})

# class LoginForm(LoginView):
#     form=loginForm()


class api(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        users=extendedUser.objects.all()
        serialize=userSerializer(users,many=True)
        return Response(serialize.data)

    def post(self,request):
        data=request.data
        data=json.dumps(data)
        data=json.loads(data)
        form_data=registrationForm(request.data)
        if form_data.is_valid():
            serialize=userSerializer(data=data)
            if serialize.is_valid():
                serialize.save()
                print('User Registered Successfully')
                data={'Status':'User Registered Successfully'}
                return Response(data)
            return redirect('login')
        else:
            form=registrationForm()
            print('Data not properly serialized')
            return render(request,'register.html',{'form':form,'form_data':form_data})

def stockList(request):
    tickers = tickers_nifty50()
    list=request.POST.get('stocks')
    info=get_company_info("BAJAJFINSV.NS")
    return render(request,'nseStockList.html',{'tickers':tickers})

def stockDetails(request):
    list=request.POST.getlist('stocks')
    # for i in list:
    #     company_info=get_quote_data(i)
    #     data.update({i:company_info})
    
    data={}
    def getData(i):
        a=get_quote_data(i)
        return get_quote_data(i)

    with ThreadPoolExecutor() as e:
        futures=[e.submit(getData , i) for i in list]

    for future,index in zip(as_completed(futures) , list):
        data.update({index:future.result()})
    return render(request,'stockDetails.html',{'data':data})


# {% for i,j in data.items %}
# {% for a,b in j.items %}
# {% if a == 'symbol' %}
# <p>{{b}}</p>
# {% endif %}
# {% endfor %}
# {% endfor %}