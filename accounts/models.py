from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render
from posts.models import Post
# from django.contrib.auth.models import User
# Create your models here.

def get_all_author_post(self):
    return self.posts.all()