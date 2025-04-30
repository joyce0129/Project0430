from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from datetime import datetime
import random

def sayhello(request):
    return HttpResponse("Hello Django")

def hello2(request,username):
    return HttpResponse("Hello Django,"+ username)

def hello3(request,username):
    #抓現在的時間 #local指的是傳所有的變數
    now= datetime.now()
    return render(request,"App01/hello3.html",locals())

def hello4(request,username):
    #抓現在的時間
    now= datetime.now()
    return render(request,"App01/hello4.html",locals())

def dice(request):
    no1=random.randint(1,6)
    no2=random.randint(1,6)
    no3=random.randint(1,6)
    return render(request,"App01/dice.html",locals())