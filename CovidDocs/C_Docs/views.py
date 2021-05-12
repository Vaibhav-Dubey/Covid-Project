from django.shortcuts import render
from django.http import HttpResponse
from .models import Notification

# Create your views here.

def Notifier(request):

    if request.method == 'POST':
        email= request.POST["email"]
        state=request.POST["state"]
        district=request.POST["district"]
        pincode=request.POST["pin"]

        person_info = Notification(email=email,state=state,district=district,pincode=pincode)
        if Notification.objects.filter(email=email).exists():
            return render(request, 'test.html')
        else:
            person_info.save()
        
    return render(request,'Notifier.html')


# def notifier_filled(request):
#     print("notifer_filled")
#     email= request.POST["email"]
#     state=request.POST["state"]
#     district=request.POST["district"]
#     pincode=request.POST["pin"]

#     person_info = Notification(email=email,state=state,district=district,pincode=pincode)

#     person_info.save()


#     return render(request,'test.html')

def index(request):
    return render(request, "test.html")