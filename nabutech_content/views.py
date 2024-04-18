from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import HomePageContent
from .models import BlogPost
from core.models import UserProfile  # Import UserProfile from core app


def home_page(request):
    
    homepage_content = HomePageContent.objects.all().first()  # Assuming there's only one instance of HomePageContent
    blog_posts = BlogPost.objects.all()
    return render(request, 'home.html', {'homepage_content': homepage_content, 'blog_posts': blog_posts})

def blog_post_detail(request, pk):

    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_post_detail.html', {'blog_post': blog_post})


def about_page(request):
    user_profile = request.user.userprofile
    return render(request, 'about.html', {'user_profile': user_profile})

def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Process the form data (e.g., send email, save to database)
        return HttpResponse('Thank you for your message!')
    return render(request, 'contact.html')