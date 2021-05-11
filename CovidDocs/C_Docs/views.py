from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Notifier(request):
    return render(request,'Notifier.html')

def index(request):
    return render(request, "test.html")