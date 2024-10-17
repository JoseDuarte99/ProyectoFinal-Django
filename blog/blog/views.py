from django.views.generic import ListView
from django.shortcuts import render

from apps.post.models import Post

# Create your views here.

class IndexPostView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    