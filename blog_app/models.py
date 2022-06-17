from urllib import request
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    Title=models.CharField(max_length=200)
    Text=models.TextField(blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    Authour=models.ForeignKey(User,on_delete=models.CASCADE)
    published_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title
        


