from django.contrib.syndication.views import Feed
from models import *

class LatestPosts(Feed):
    title = "Jack Moxon's musings"
    link = "/blog/"
    description = "Latest posts..."
    
    def items(self):
        return Post.objects.order_by('-datetime')[:3]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.subtitle
    
    def item_link(self, item):
        return "/blog/"
