from django.db import models

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
