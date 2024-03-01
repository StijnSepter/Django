from django.db import models
from django.core.files import File
import markdown

class projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1024)
    image = models.ImageField(upload_to='static/images/')
    url = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)

class skill(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    image = models.TextField(max_length=255)
    date = models.DateField(auto_now=True)
    id = models.AutoField(primary_key=True)