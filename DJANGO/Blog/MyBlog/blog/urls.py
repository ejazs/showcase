from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, share_post,SharePostView \
  , GetPostByTags

from .feeds import PostFeed

app_name = 'post'
urlpatterns = [
  path('', PostListView.as_view(), name='home'),
  path('tag/', GetPostByTags.as_view(), name='tag'),
  path('create/', PostCreateView.as_view(), name='create'),
  path('detail/<slug:slug>/',PostDetailView.as_view(), name='detail'),
  path('detail/<slug:slug>/update/',PostUpdateView.as_view(), name='update'),
  path('detail/<slug:slug>/share/', SharePostView.as_view(), name='share'),
  path('feeds/', PostFeed(), name='post_feed')
]