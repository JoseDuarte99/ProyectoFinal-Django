from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Comment
from .forms import CreatePostForm, UpdatePostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(post_id=self.kwargs['id'])
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_id = request.user.id
            comment.post_id = self.kwargs['id']
            comment.save()
            return redirect('apps:post_individual', id=self.kwargs['id'])
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return render(request, 'some_template.html', context)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post/comments_create.html'
    success_url = 'post/comments'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs['post_id']
        return super().form_valid(form)


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


class Category(TemplateView):
    template_name = 'category.html'