from django.urls import path
from .views import *

app_name = 'apps.posts'

urlpatterns= [
    path('', PostListView.as_view(), name='posts'),
    path('<int:id>/', PostDetailView.as_view(), name='post_individual'),
]