from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'index.html') 