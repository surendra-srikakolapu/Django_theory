from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First name", max_length="100")
    last_name = forms.CharField(label="Last name", max_length="100")
    username = forms.CharField(label="Username")
    password1 = forms.CharField(label='password')
    password2 = forms.CharField(
        label='Re-Password')

    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ['username', 'last_name', 'first_name', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['dob', 'image']
