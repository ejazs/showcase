from django.urls import path
from .views import test

urlpatterns = [
  path('<int:pk>/comments', test, name='test'),
]