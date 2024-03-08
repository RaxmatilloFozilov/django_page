from django.db import models
from django.contrib.auth.models import User


class Kino(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class Kompyuter(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return self
class City(models.Model):
    name = models.CharField(max_length=60)
    field =models.CharField(max_length=500)

class Book(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    author = models.ForeignKey(Kino, on_delete=models.CASCADE)
    comments = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

class University(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
