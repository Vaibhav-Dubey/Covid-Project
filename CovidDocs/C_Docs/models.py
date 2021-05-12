from django.db import models

# Create your models here.

class Notification(models.Model):
    email=models.CharField(max_length=200)
    state=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    pincode=models.CharField(max_length=20)

    def __str__(self):
        return self.email