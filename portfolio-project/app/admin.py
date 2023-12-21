from django.contrib import admin
from .models import TodoItem, urlItem, projects

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(urlItem)

class adminProjects(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(projects, adminProjects)