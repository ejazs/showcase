from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=120)
    last_name = forms.CharField(max_length=120)
    email = forms.EmailField()

    class Meta:
      model = User
      fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']