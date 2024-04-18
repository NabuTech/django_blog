# In nabutech_content/models.py

from django.db import models
from markdownx.models import MarkdownxField

def upload_location(instance, filename):
    return f'nabutech_content/images/{filename}'

class HomePageContent(models.Model):
    image = models.ImageField(upload_to=upload_location)
    introduction = models.TextField()

    def __str__(self):
        return "HomePage Content"

class BlogPost (models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    content = MarkdownxField()
    author = models.ForeignKey('core.UserProfile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
