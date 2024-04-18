from django import forms
from .models import HomePageContent, BlogPost

class HomePageContentForm(forms.ModelForm):
    class Meta:
        model = HomePageContent
        fields = ['image', 'introduction']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'description', 'content', 'author']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data['name']
        # Perform any additional validation for the name field
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        return name

    def clean_message(self):
        message = self.cleaned_data['message']
        # Perform any additional validation for the message field
        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return message