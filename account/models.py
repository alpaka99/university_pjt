from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    major1 = models.TextField(max_length=10,blank=True,null=True)
    major2 = models.TextField(max_length=10,blank=True,null=True)


