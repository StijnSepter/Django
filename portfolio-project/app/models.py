from django.db import models
from django.core.files import File
import os
import urllib

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class urlItem(models.Model):
    URL = models.CharField(max_length=255)

class projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/images/')
    url = models.CharField(max_length=200)
    # created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now=True)

# def get_remote_image(self):
#     if self.image_url and not self.image:
#         result = urllib.urlretrieve(self.image)
#         self.image.save(
#             os.path.basename(self.image_url),
#             File(open(result[0]))
#         )
#         self.save()