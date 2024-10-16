from django import forms
from .models import Post
from django.views.generic.edit import UpdateView


class CreatePostForm(forms.ModelForm):
    
    class Meta():
        model = Post
        fields = ['title','subtitle','text','category','image']


class UpdatePostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'text', 'category', 'image']