from django.shortcuts import render, HttpResponse
from .models import projects, slideshow
from django.template import loader
from django.conf import settings
from django.conf.urls.static import static


def home(reqeust):
    project = projects.objects.all()
    slideshowItem = slideshow.objects.all()
    return render(reqeust, "home.html", {"home": project})
#! home is wat ik gebruik in home.html om data te laten zien
