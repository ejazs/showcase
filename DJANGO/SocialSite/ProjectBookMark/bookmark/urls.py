from django.urls import path
from .views import  Home, image_create_view, ImageCreateView

app_name = 'bookmark'

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('image/', ImageCreateView.as_view(), name='image'),
  path('bookmark/', image_create_view, name= 'bookmark'),
  
]

