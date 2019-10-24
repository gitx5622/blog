from django.conf import settings
from django.db import models
from django.db.models import Q

User = settings.AUTH_USER_MODEL

class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1,null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    publish_date = models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-publish_date','-updated_at','-timestamp']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f"/blog/{self.slug}"
    
    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"
    
    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"
    
    def search(self,query):
        lookup = (Q(title__icontains=query)|
                  Q(content__icontains=query)|
                  Q(slug__icontains=query))
        return self.filter(lookup)
    

        