from django.urls import path
from django.urls import include
from django.conf import settings
from mySite import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('repo', views.repo, name='repo'),
    path('current_projects', views.curprojects, name='current_projects'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)