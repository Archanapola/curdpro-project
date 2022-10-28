from django.db import models

# Create your models here.
class sdata (models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    mobile=models.IntegerField()
    iname=models.CharField(max_length=30)
    assignment1=models.IntegerField()
    assignment2=models.IntegerField()
    assignment3=models.IntegerField()
