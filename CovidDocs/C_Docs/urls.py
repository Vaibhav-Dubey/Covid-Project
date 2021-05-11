from django.urls import path

from . import views

urlpatterns = [
    path('Notifier', views.Notifier, name='notifier'),
]