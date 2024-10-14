from django.urls import path
from .views import *

urlpatterns= [
    path('', PostListView.as_view(), name='posts'),
    path('<int:id>/', PostDetailView.as_view(), name='post_individual'),
]