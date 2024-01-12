from django.contrib import admin
from .models import projects, slideshow

# Register your models here.
admin.site.register(slideshow)

class adminProjects(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(projects, adminProjects)