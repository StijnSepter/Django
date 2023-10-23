from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class urlItem(models.Model):
    URL = models.CharField(max_length=255)