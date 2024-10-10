from django.shortcuts import render
from .models import Post

# Create your views here.

def post(request):
    post = Post.objects.all()
    return render(request, 'posts.html', {'post': post})