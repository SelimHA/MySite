from django.db import models
from datetime import datetime
# Create your models here.
class Project(models.Model):
    TITLE_MAX_LENGTH = 64
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    text = models.TextField()
    language=models.CharField(max_length=TITLE_MAX_LENGTH, default="File")
    def __str__(self):
        return f"{self.id}: {self.title}"

class projectImage(models.Model):
    title = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images', blank=True)
    def __str__(self):
        return f"{self.id}: {self.title}"

class repoContent(models.Model):
    TITLE_MAX_LENGTH = 256
    title = models.CharField(max_length=TITLE_MAX_LENGTH, default ="No title")
    language=models.CharField(max_length=TITLE_MAX_LENGTH, null=True,default="File")
    description = models.TextField(default="Missing description")
    link = models.TextField(default="#")
    date_created = models.DateTimeField(default = datetime.now)
    date_updated = models.DateTimeField(default = datetime.now)
    def __str__(self): 
        return self.title

class contributors(models.Model):
    TITLE_MAX_LENGTH = 64
    title = models.ForeignKey(repoContent, on_delete=models.CASCADE)
    contribName = models.CharField(max_length=TITLE_MAX_LENGTH, default = "Anon")
    commits = models.CharField(max_length=TITLE_MAX_LENGTH, default="0")
    def __str__(self):
        return f"{self.id}: {self.title}"

class Languages(models.Model):
    TITLE_MAX_LENGTH = 256
    language = models.CharField(max_length=TITLE_MAX_LENGTH, null=True,default="File")
    usage = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.id}: {self.language}"