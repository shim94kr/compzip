from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, PasswordInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'password': PasswordInput()
        }