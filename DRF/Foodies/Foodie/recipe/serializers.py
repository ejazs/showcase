from rest_framework import serializers
from .models import Recipe
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name'] 

class RecipeCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Recipe
    fields = ['title', 'author', 'ingredients', 'method', 'tips']

class RecipeListSerializer(serializers.ModelSerializer):
  ingredients = serializers.SerializerMethodField()
  author = serializers.SerializerMethodField()
  def get_author(self,obj):
    print(obj.author)
    user = User.objects.filter(username=obj.author).first()
    return UserSerializer(user).data

  def get_ingredients(self, obj):
    return obj.ingredients[:100]

  class Meta:    
    model = Recipe
    fields = ['title','author','ingredients','method','tips']

class RecipeDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Recipe
    fields = ['title', 'author', 'ingredients','method', 'tips']
