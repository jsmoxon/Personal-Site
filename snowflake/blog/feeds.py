from django.contrib.syndication.views import Feed
from models import *

class LatestPosts(Feed):
    title = "Jack Moxon's Blog"
    link = "http://www.jackmoxon.com/blog/"
    description = "Latest blog posts..."
    
    def items(self):
        return Post.objects.order_by('-datetime')[:50]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.subtitle
    
    def item_link(self, item):
        return "http://jackmoxon.com/blog/"+str(item.id)
