from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=500)
    topic = models.CharField(max_length=200)
    description = models.TextField()
    excerpt = models.TextField(max_length=300)
    viewer = models.PositiveIntegerField(default=0)
    picture = models.ImageField(upload_to='Blog_picture')

