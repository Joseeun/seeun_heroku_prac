from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from .models import UserInformation

class UserInformationForm(forms.ModelForm):
    class Meta:
        model = UserInformation
        fields = ('age', 'address')