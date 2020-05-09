from rest_framework import serializers
from .models import Post

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name']

class PostListSerializer(serializers.ModelSerializer):
  author = serializers.SerializerMethodField()
  url = serializers.HyperlinkedIdentityField(view_name= 'posts:post_detail', lookup_field = 'slug')
  class Meta:
    model = Post
    fields = ['url', 'title', 'author', 'body', 'created_at'] 
  
  def get_author(self, obj):
    return str('{} {}'.format(obj.author.first_name, obj.author.last_name))
  
  

class PostDetailSerializer(serializers.ModelSerializer):

  author = serializers.SerializerMethodField()
  url = serializers.HyperlinkedIdentityField(view_name= 'posts:post_detail', lookup_field=('slug'))
  delete_url = serializers.HyperlinkedIdentityField(view_name='posts:post_delete', lookup_field='slug')

  class Meta:
    model = Post
    fields = ['url','title', 'author', 'body', 'created_at','delete_url'] 
  
  def get_author(self, obj):
    user = UserSerializer(User.objects.filter(username=obj.author).first()).data
    return user

class PostCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ['title',  'body']
