from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BLANK_CHOICE_DASH

class UserInformation(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)