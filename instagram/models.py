from django.db import models
from vote.models import VoteModel
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here

class Image(VoteModel,models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    caption = models.CharField(max_length=200)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    # profile = models.ForeignKey(User, on_delete=models.CASCADE)
    like_add = models.PositiveIntegerField(default=0)
    