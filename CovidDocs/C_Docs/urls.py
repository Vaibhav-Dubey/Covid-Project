from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('Notifier', views.Notifier, name='notifier'),
    path('notifier_filled',views.notifier_filled,name="bleh"),
]