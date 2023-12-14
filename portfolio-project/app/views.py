from django.shortcuts import render, HttpResponse
from .models import TodoItem, urlItem, projects
from django.template import loader
from django.conf import settings
from django.conf.urls.static import static

def home(reqeust):
    project = projects.objects.all()
    return render(reqeust, "home.html", {"home": project})
#! home is wat ik gebruik in home.html om data te laten zien


def todolist(reqeust):
    items = TodoItem.objects.all()
    return render(reqeust, "todolist.html", {"todolist": items})