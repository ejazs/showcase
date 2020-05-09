from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.utils.text import  slugify
from django.urls import reverse
# Create your models here.

User = settings.AUTH_USER_MODEL

class Post(models.Model):
  title = models.CharField(max_length=120)
  slug  = models.SlugField(max_length=1000)
  body  = models.TextField()
  author= models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  # def get_absolute_url(self):
  #   return reverse('posts:post_detail', kwargs={'slug':self.slug})

  def __str__(self):
    return str(self.title)


def save_slug(sender, instance, created, *args, **kwargs):
  print('In presave', instance.id)
  if created:
      # max_id = Post.objects.only('pk').last() 
      # max_id = max_id.pk
      instance.slug = '{}-{}'.format(slugify(instance.title), str(instance.id))
      
      instance.save()
      print('In save', instance.id)

post_save.connect(save_slug, sender=Post)
