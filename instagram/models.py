from django.db import models
from vote.models import VoteModel
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from PIL import Image
# Create your models here

class Image(VoteModel,models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    caption = models.CharField(max_length=200)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    like_add = models.PositiveIntegerField(default=0)
    

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default="profile.jpg", upload_to="profile_pics")
  
  
  def __str__(self):
    return ("{} profile").format(self.user.username)
  def save(self):
    super().save()
    img = Image.open(self.image.path)
    if img.height > 300 or img.width > 300:
      output_size = (300, 300)
      img.thumbnail(output_size)
      img.save(self.image.path)