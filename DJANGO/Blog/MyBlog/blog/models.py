from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.db.models import Q
from django.urls import reverse
# Create your models here.

User = settings.AUTH_USER_MODEL

class Tag(models.Model):
  tag = models.CharField(max_length=120)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.tag

class PostModelManager(models.Manager):
  def get_queryset(self):
    qs = super(PostModelManager, self).get_queryset()
    return qs.filter(status='published')

  def search(self, search_query):
    qs = self.get_queryset()
    qs = qs.filter(
      Q(title__icontains=search_query) |
      Q(body__icontains = search_query) |
      Q(author__username=search_query)
    )
    return qs
    

class Post(models.Model):
  STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published')
  )
  title = models.CharField(max_length=120)
  slug = models.SlugField(null=True, blank=True)
  author = models.ForeignKey(to=User, on_delete=models.CASCADE)
  body = models.TextField()
  publish = models.DateTimeField(default=timezone.now())
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  status = models.CharField(max_length=120, choices = STATUS_CHOICES)
  tag = models.ManyToManyField(to=Tag, related_name='tagged', blank=True, null=True)

  objects = models.Manager()
  published = PostModelManager()

  class Meta:
    ordering = ['-created']

  def __str__(self):
    return str(self.title)

  def save(self, *args, **kwargs):
    if self.slug is None:
      super(Post, self).save(*args, **kwargs)
      # print('self.id',self.id)
      self.slug = '{}-{}'.format(str(slugify(self.title)), str(self.id))
    super(Post, self).save(*args, **kwargs)
   # super(Post, self).save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse('post:detail', kwargs={'slug':self.slug})

  def get_comments(self):
    return Comment.actives.filter(post=self)

  def get_tags(self):
    return self.tag.all()
    

class CommentManager(models.Manager):
  def get_queryset(self):
    qs = super(CommentManager, self).get_queryset()
    return qs.filter(active=True)

class Comment(models.Model):
  post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')
  name = models.CharField(max_length=120)
  email = models.EmailField()
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  objects = models.Manager()
  actives  = CommentManager()

  class Meta:
    ordering = ['-created']

  def __str__(self):
    return 'comment by {} on {}'.format(self.name, self.post)


