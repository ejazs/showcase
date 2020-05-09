from django.db import models

class Person(models.Model):
  name = models.CharField(max_length=120)
  address = models.TextField()

  def __str__(self):
    return str(self.name)