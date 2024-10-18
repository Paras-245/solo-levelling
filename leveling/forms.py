from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Quest

class SignupForm(UserCreationForm):
    goal = forms.CharField(max_length=100,required=True)
    goal_progress = forms.CharField(max_length=100,required=True)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

