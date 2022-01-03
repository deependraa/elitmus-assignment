from enum import auto
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render

class Post(models.Model):
    content = models.TextField(default=None)
    title = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')

    def __str__(self):
        return str(self.content)

    def num_comments(self):
        return self.comment_set.all.count()
    class Meta:
        ordering = ['-created']

    
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)


