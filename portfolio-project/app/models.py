from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class urlItem(models.Model):
    URL = models.CharField(max_length=255)

class projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='django files/covers')
    url = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)