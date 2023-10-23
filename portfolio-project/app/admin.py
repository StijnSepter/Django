from django.contrib import admin
from .models import TodoItem, urlItem

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(urlItem)