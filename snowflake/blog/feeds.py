from django.contrib.syndication.feeds import Feed
from models import *

class LatestPosts(Feed):
    title = "Post"
    link = "/blog/"
    description = "Latest posts..."
    
    def items(self):
        return Post.objects.order_by('-pub_date')[:50]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.description
