from django.urls import path
from django.urls import include
from mySite import views

urlpatterns = [
    path('', views.index, name='index'),
]