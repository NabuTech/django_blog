from django.contrib import admin
from .models import HomePageContent, BlogPost
from .forms import HomePageContentForm, BlogPostForm


class HomePageContentAdmin(admin.ModelAdmin):
    form = HomePageContentForm

admin.site.register(HomePageContent, HomePageContentAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostForm

admin.site.register(BlogPost, BlogPostAdmin)