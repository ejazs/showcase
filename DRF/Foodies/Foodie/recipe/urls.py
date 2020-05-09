from django.urls import path
from .views import RecipeListAPIView, RecipeDetailAPIView, RecipeCreateAPIView, RecipeUpdateAPIView,RecipeDeleteView
urlpatterns = [
  path('', RecipeListAPIView.as_view(),name='recipes'),
  path('create/', RecipeCreateAPIView.as_view(),name='create'),
  path('<id>/', RecipeDetailAPIView.as_view(), name='recipes_detail'),
  path('<id>/edit/', RecipeUpdateAPIView.as_view(), name='recipes_edit'),
  path('<id>/delete/', RecipeDeleteView.as_view(), name='recipes_delete')
]