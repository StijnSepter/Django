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
    title_skills = models.CharField(max_length=200)
    description_skills = models.CharField(max_length=255)
    icon_skills = models.TextField(max_length=255)
    date_skills = models.DateField(auto_now=True)
    id_skills = models.AutoField(primary_key=True)

