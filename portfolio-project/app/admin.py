from django.contrib import admin
from .models import projects, skill

# Register your models here.
admin.site.register(skill),

class adminProjects(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(projects, adminProjects)