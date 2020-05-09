from django.shortcuts import render
from .models import  Recipe
from .serializers import  RecipeListSerializer,RecipeDetailSerializer, RecipeCreateSerializer
from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView,DestroyAPIView
                                    )
# Create your views here.

class RecipeListAPIView(ListAPIView):
  queryset = Recipe.objects.all()
  serializer_class = RecipeListSerializer

class RecipeDetailAPIView(RetrieveAPIView):
  queryset = Recipe.objects.all()
  serializer_class = RecipeDetailSerializer
  lookup_field = 'id'

class RecipeCreateAPIView(CreateAPIView):
  queryset = Recipe.objects.all()
  serializer_class = RecipeCreateSerializer

class RecipeUpdateAPIView(RetrieveUpdateAPIView):
  queryset = Recipe.objects.all()
  serializer_class = RecipeCreateSerializer
  lookup_field = 'id'

class RecipeDeleteView(DestroyAPIView):
  queryset = Recipe.objects.all()
  serializer_class = RecipeDetailSerializer
  lookup_field = 'id'