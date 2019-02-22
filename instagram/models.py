from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photos = models.ImageField(upload_to='../media/',default='default.jpg',height_field=None,width_field=None,max_length=100000)
    content = models.TextField(blank=True)
    like = models.BooleanField(default=False,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '[{}] {}'.format(self.user.username, self.title)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    contenet = models.TextField()
    cretaed_at = models.DateTimeField(auto_now_add=True)

class FileUploader(models.Model):
    file = models.FileField()
    name = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now=True, db_index=True)
    owner = models.ForeignKey('auth.User', related_name='uploaded_files', on_delete=models.CASCADE)
    size = models.IntegerField(default=0)

    