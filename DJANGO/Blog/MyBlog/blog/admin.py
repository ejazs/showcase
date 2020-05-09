from django.contrib import admin
from .models import Post, Comment, Tag
# Register your models here.

admin.site.register(Comment)
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
  
  fields = ['title', 'author', 'body', 'publish', 'status', 'tag']

admin.site.register(Post, PostAdmin)