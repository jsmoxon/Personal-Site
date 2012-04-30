from django.db import models

class Tags(models.Model):
    tag = models.CharField(max_length=200)
    def __unicode__(self):
        return str(self.tag)

class BlogImage(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=2000, null=True, blank=True)
    def __unicode__(self):
        return str(self.image)
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    body = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    votes = models.IntegerField(blank=True, null=True, default=0)
    feeling = models.CharField(max_length=500, null=True, blank=True)
    song = models.CharField(max_length=500, null=True, blank=True)
    iframe = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=2000, null=True, blank=True)
    images = models.ManyToManyField(BlogImage, blank=True, null=True)
    tags = models.ManyToManyField(Tags, blank=True, null=True)
    def __unicode__(self):
        return str(self.title)
    
    
