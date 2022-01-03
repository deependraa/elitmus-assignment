from django.db import models
from datetime import datetime

class advertiser(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    
