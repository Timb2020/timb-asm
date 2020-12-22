from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Asset
from django.forms import ModelForm


class registerForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username', 'email','password1','password2']

class add_assetForm(ModelForm):
    class Meta:
        model= Asset
        fields = '__all__'