from django.db import models
from django.conf import settings
from django.utils.text import slugify
# Create your models here.

User = settings.AUTH_USER_MODEL

class Image(models.Model):
  user = models.ForeignKey(to=User, on_delete=models.CASCADE)
  title = models.CharField(max_length=120)
  slug = models.SlugField(max_length=254)
  url = models.URLField()
  image = models.ImageField(upload_to='images')
  description = models.TextField(null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  user_likes = models.ManyToManyField(to=User, related_name='images_liked', null=True, blank=True)

  def __str__(self):
    return str(self.title)

  def save(self, **kwargs):
    if not self.slug:
      super(Image, self).save(**kwargs)
      self.slug = '{}-{}'.format(slugify(self.title), str(self.id))
    super(Image, self).save(**kwargs)