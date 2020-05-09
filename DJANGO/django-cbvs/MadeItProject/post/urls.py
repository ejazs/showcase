from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
  path('', PostListView.as_view(), name='post-list'),
  path('create/', PostCreateView.as_view(), name='post-create'),
  path('post/<slug>/', PostDetailView.as_view(), name='post-detail'),
  path('post/<slug>/edit', PostUpdateView.as_view(), name='post-edit'),
  path('post/<slug>/delete', PostDeleteView.as_view(), name='post-delete'),
  
]



Start with 