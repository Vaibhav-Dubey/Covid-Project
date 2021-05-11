from django.shortcuts import render
from django.http import HttpResponse
from .models import Notification

# Create your views here.

def Notifier(request):
    return render(request,'Notifier.html')


def notifier_filled(request):
    print("notifer_filled")
    email= request.POST["email"]
    state=request.POST["state"]
    district=request.POST["district"]
    pincode=request.POST["pin"]

    person_info = Notification(email=email,state=state,district=district,pincode=pincode)

    person_info.save()


    return render(request,'Notifier.html')

def index(request):
    return render(request, "test.html")