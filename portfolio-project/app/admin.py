from django.contrib import admin
from .models import TodoItem, urlItem, projects

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(urlItem)
admin.site.register(projects)