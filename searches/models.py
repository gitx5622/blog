from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class SearchQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True,null=True)
    query = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)