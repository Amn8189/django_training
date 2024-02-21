from django.db import models

# Create your models here.
class student(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phonenumber = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    