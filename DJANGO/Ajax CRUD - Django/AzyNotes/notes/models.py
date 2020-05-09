from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class Note(models.Model):
  title = models.CharField(max_length=120)
  status = models.BooleanField(default=False)
  created_by = models.ForeignKey(to=User, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.title)
    