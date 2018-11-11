from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post

class LatestPostsFeed(Feed):
    title = 'Latest posts'
    link = '/feed/'
    description = 'The latest posts on borisideler.be'

    def items(self):
        return Post.objects.all().order_by('-date_published')

    def item_title(self, item):
        return item.title    
    
    def item_link(self, item):
        return reverse('blog:post', args=[item.pk])