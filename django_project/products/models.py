from django.db import models


# Create your models here.

class Product(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=100)
    Image = models.CharField(max_length=200)


class User(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Password = models.CharField(max_length=20)
