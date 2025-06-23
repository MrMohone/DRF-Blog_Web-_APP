from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
   bio = models.TextField(blank=True, null=True)
   profile_picture = models.ImageField(upload_to='profile_img/', blank=True, null=True)
   facebook = models.URLField(max_length=225, blank=True, null=True)
   youtube = models.URLField(max_length=225, blank=True, null=True)
   instagram = models.URLField(max_length=225, blank=True, null=True)
   tiwtter = models.URLField(max_length=225, blank=True, null=True)
   
   def __str__(self):
       return self.username
   

   
