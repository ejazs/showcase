from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post

class PostFeed(Feed):
  title = "EZ's Blog"
  link  = "/"
  description = "Blog posts from EZ"

  def items(self):
    return Post.published.all()

  def item_title(self, item):
    return item.title

  def item_description(self, item):
    return truncatewords(item.body, 30)
    