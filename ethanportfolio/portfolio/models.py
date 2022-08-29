from django.db import models
from ethanportfolio.settings import MEDIA_ROOT


class Project(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media', null=True)
    description = models.TextField()
    page_link = models.CharField(max_length=255, null=True)
    visible = models.BooleanField(default=False)

    @classmethod
    def all_visible(cls):
        return Project.objects.filter(visible=True)