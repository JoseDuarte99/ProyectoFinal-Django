from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import CreatePostForm, UpdatePostForm
from django.urls import reverse_lazy

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post 
    template_name = 'posts/post_individual.html'
    context_object_name = 'posts'
    pk_url_kwarg = 'id'
    queryset = Post.objects.all() # Redundante porque DetailView lo usara por defecto.

class PostCreateView(CreateView):
    form_class = CreatePostForm
    template_name = 'posts/post_create.html'
    model = Post
    success_url = reverse_lazy('apps.posts:posts')

class PostUpdateView(UpdateView):
    form_class = UpdatePostForm
    template_name = 'posts/post_update.html'
    model = Post
    success_url = reverse_lazy('apps.posts:posts')
    pk_url_kwarg = 'id'
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('apps.posts:posts')
    pk_url_kwarg = 'id'