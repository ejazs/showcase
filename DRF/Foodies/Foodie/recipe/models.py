from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL
class Recipe(models.Model):
  title = models.CharField(max_length=120)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  ingredients = models.TextField()
  method = models.TextField()
  tips = models.CharField(max_length=255)

  def __str__(self):
    return str(self.title)

