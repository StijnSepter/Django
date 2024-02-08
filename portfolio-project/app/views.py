from django.shortcuts import render, HttpResponse
from .models import projects, skill
from django.template import loader
from django.conf import settings
from django.conf.urls.static import static


def home(reqeust):
    project = projects.objects.all()
    return render(reqeust, "home.html", {"home": project})
#! here I use slideshow to get the data from the database and pass it to the home.html file


def Myskills(reqeust):
    skillsItem = skill.objects.all()
    return render(reqeust, "home.html", {"Myskills": skillsItem}),
   