from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photos = models.ImageField(default='default.jpg')
    latitude = models.FloatField()
    longitude = models.FloatField()
    content = models.TextField(blank=True)
    like = models.BooleanField(default=False,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return '[{}] {}'.format(self.user.username, self.title)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    