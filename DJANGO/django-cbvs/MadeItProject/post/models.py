from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

User = settings.AUTH_USER_MODEL

class Post(models.Model):
  title = models.CharField(max_length=180)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  cover = models.ImageField(upload_to='covers')
  content = models.TextField()
  slug = models.SlugField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.title)

  def get_absolute_url(self):
    return reverse('post:post-detail', kwargs={'slug':self.slug})

class Comment(models.Model):
  content = models.CharField(max_length=180)
  post    = models.ForeignKey(Post, on_delete=models.CASCADE)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.content)



def create_slug(instance, created, *args, **kwargs):
  if created:
    instance.slug = '{}-{}'.format(slugify(instance.title), str(instance.id))
    instance.save()

post_save.connect(create_slug, sender=Post)