from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings
from mySite.models import projectImage, Project, repoContent, contributors, Languages
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    languages = Languages.objects.all()
    context_dict = {"languages":getTotalLanguages(languages)}
    return render(request, 'index.html', context_dict) 

def getTotalLanguages(languages):
    dictReturn = {}
    for curLang in languages:
        dictReturn[curLang.language]=curLang.usage
    return dictReturn

def repo(request):
    data = repoContent.objects.all()
    data_list = createDict(data)
    paginator = Paginator(data_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context_dict ={"project_data": page_obj}
    return render(request, 'mySite/repo.html', context_dict)

def curprojects(request):
    context_dict = {"project":[]}
    projects = Project.objects.all()
    for project in projects:
        curProject = {}
        curProject["name"] = project.title
        curProject["details"] = project.text
        curProject["language_icon"]= getIcon(project.language)
        images = projectImage.objects.all().filter(title=project)
        curProject["images"]=images
        context_dict["project"].append(curProject)
    return render(request, 'mySite/current_projects.html', context_dict)

def createDict(data):
    data_list = []
    for cur in data:
        cur_dict = {}
        cur_dict["name"]=cur.title
        cur_dict["language_icon"]=getIcon(cur.language)
        cur_dict["description"]=cur.description
        cur_dict["date"]=cur.date_created
        contribs = contributors.objects.all().filter(title=cur)
        cur_contribs = []
        for cur_contrib in contribs:
            contrib_dict = {}
            contrib_dict["name"]=cur_contrib.contribName
            contrib_dict["contribution"]=cur_contrib.commits
            cur_contribs.append(contrib_dict)
        cur_dict["contributors"]= cur_contribs
        data_list.append(cur_dict)
    return data_list

def getIcon(languageName):
        if(languageName=="Java"):
                return "fab fa-java"
        elif(languageName=="Python"):
                return "fab fa-python"
        elif(languageName=="HTML"):
                 return "fab fa-html5"
        elif(languageName=="Kotlin"):
                return "fab fa-android"
        elif(languageName=="Swift"):
                return "fas fa-apple-alt"
        elif(languageName=="C" or languageName=="C++" or languageName=="C#"):
                return "fab fa-cuttlefish"
        else:
                return "fas fa-file"

