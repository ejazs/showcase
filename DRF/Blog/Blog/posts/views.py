from django.shortcuts import render
from .serializers import PostListSerializer, PostDetailSerializer, PostCreateSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, CreateAPIView
from .models import Post
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import  IsOwnerOrReadOnly
# Create your views here.

class PostListAPIView(ListAPIView):
  queryset = Post.objects.all()
  serializer_class = PostListSerializer
  permission_classes = [AllowAny]

class PostDetailAPIView(RetrieveUpdateAPIView):
  queryset = Post.objects.all()
  lookup_field = 'slug'
  serializer_class = PostDetailSerializer
  permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,]

class PostDeleteAPIView(RetrieveDestroyAPIView):
  queryset = Post.objects.all()
  lookup_field= 'slug'
  serializer_class = PostDetailSerializer
  permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,]

class PostCreateAPIView(CreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostCreateSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(author = self.request.user)