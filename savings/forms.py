from django.forms import ModelForm
from .models import Aim
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class AimsForm(ModelForm):
    class Meta:
        model = Aim
        fields = [
            'aim',
            'data',
            'price',
        ]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
