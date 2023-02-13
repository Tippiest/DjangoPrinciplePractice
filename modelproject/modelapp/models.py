from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.IntegerField(null=False)

#Menu Category Table
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=100)

#Menu Table
class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, related_name="category_name")

#Query Set Practice

class Customer(models.Model):
    name = models.CharField(max_length=255)

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='Vehicle'
    )

#practice dynamic form
class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    time_log = models.TimeField()