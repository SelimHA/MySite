from django.urls import path
from django.urls import include
from mySite import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('repo', views.repo, name='repo'),
    path('current_projects', views.curprojects, name='current_projects'),
]