from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings
from mySite.models import projectImage, Project
from mySite.GitGetter import *
# Create your views here.
def index(request):
    context_dict = {"languages": getTotalLanguages()}
    return render(request, 'index.html', context_dict) 

def repo(request):
    context_dict = {"project_data": getAllProjectDetails()}
    return render(request, 'mySite/repo.html', context_dict)

def curprojects(request):
    context_dict = {"project":[]}
    projects = Project.objects.all()
    for project in projects:
        curProject = {}
        curProject["name"] = project.title
        curProject["details"] = project.text
        curProject["language_icon"]= getIcon(project.language)
       # images = projectImage.objects.all().filter(title=curProject["name"])
        #curProject["images"]=images
        context_dict["project"].append(curProject)
    return render(request, 'mySite/current_projects.html', context_dict)