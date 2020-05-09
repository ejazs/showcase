from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
from markdown import markdown

register = template.Library()

@register.simple_tag
def total_posts():
  return Post.published.count()

@register.inclusion_tag('recent.html')
def most_recent(post=3):
  context  = {"recent_posts": Post.published.all().order_by('-id')[:post]}
  return context

@register.simple_tag
def most_commented(count=3):
  qs = Post.published.annotate(total_comment=Count('comments')).order_by('-total_comment')[:count]
  return qs

# Filters

@register.filter(name='markdown')
def markdown_format(text):
  return mark_safe(markdown(text))