from django.urls import path, re_path
from .views import  PostListAPIView, PostDetailAPIView, PostDeleteAPIView, PostCreateAPIView
urlpatterns = [
  path('', PostListAPIView.as_view(), name='post_list'),
  path('create/', PostCreateAPIView.as_view(), name='post_create'),
  path('posts/<slug>/', PostDetailAPIView.as_view(), name='post_detail'),
  path('posts/<slug>/delete/', PostDeleteAPIView.as_view(), name='post_delete')
]