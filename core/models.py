from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    about = models.TextField(blank=True)
    twitter_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.user.username
