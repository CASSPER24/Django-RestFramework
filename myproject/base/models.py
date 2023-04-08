from django.db import models


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=50)
    created= models.DateField(auto_now=True)



class Student(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    age = models.IntegerField()
    course = models.CharField(max_length=30)
    tuition = models.FloatField()
    featured_item = models.ForeignKey('Item', on_delete=models.SET_NULL, null=True)