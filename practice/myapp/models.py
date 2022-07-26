from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userprofileinfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    userurl=models.URLField(blank=True)
    picture=models.ImageField(upload_to="pictures",blank=True)

    def __str__(self):
        return self.user.username
