from django.urls import path
from .views import home_page, blog_post_detail, about_page, contact_page

urlpatterns = [
    path('', home_page, name='home'),
    path('blog/<int:pk>/', blog_post_detail, name='blog_post_detail'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
]
