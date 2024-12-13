from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, default='Untitled')
    author = models.ForeignKey(
        "auth.User", on_delete = models.CASCADE,default=1
    )
    body = models.TextField()
    
    def __str__(self):
        return self.title
    