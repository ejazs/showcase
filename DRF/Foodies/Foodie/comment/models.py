from django.db import models
from recipe.models import Recipe
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class Comment(models.Model):
  text =  models.CharField(max_length=120)
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  