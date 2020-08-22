from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    street_address = models.CharField(max_length=100)

class Library(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, related_name="author")
    location = models.ForeignKey(Library)
    readers = models.ManyToManyField(User, related_name="reader")
