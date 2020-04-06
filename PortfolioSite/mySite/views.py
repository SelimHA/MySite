from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings
from mySite.GitGetter import *
# Create your views here.
def index(request):
    context_dict = {"languages": getTotalLanguages()}
    return render(request, 'index.html', context_dict) 