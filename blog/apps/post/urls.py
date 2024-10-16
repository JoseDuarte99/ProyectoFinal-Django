from django.urls import path
from .views import *

app_name = 'apps.posts'

urlpatterns= [
    path('', PostListView.as_view(), name='posts'),
    path('<int:id>/', PostDetailView.as_view(), name='post_individual'),
    path('CreatePost/', PostCreateView.as_view(), name='posts_create'),
    path('UpdatePost/<int:id>/', PostUpdateView.as_view(), name='post_update'),
    path('DeletePost/<int:id>/', PostDeleteView.as_view(), name='post_delete'),
]