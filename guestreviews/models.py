from django.db import models

# Create your models here.
class admini(models.Model):
    Firstname =models.CharField(max_length=120)
    Lastname = models.CharField(max_length=50)
    Address  = models.CharField(max_length=50)
    Email    = models.EmailField(max_length=20)
    Username = models.CharField(max_length=12)
    Password = models.CharField(max_length=8)
    Mobile   = models.IntegerField(max_length=12)

class guest(models.Model):
    Name    = models.CharField(max_length=12)
    Address = models.CharField(max_length=50)
    City    = models.CharField(max_length=20)

class public(models.Model):
    Name    = models.CharField(max_length=12)
    Address = models.CharField(max_length=50)
    City    = models.CharField(max_length=20)


class library(models.Model):
    Name=models.CharField(max_length=12)
    Address=models.CharField(max_length=50)
    City=models.CharField(max_length=20)

class Book(models.Model):
    title=models.CharField(max_length=120)
