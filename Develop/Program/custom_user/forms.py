from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from . import models

class CustomUserForm(UserCreationForm):
    class Meta:
        model = models.CustomUsers
        fields = (
            'email', 'gender', 'phone_number', 
            'address1', 'address2', 'city', 'postal_code',
            'province', 'country', 'first_name', 'last_name'
        )
        
class LoginForm(AuthenticationForm):
    pass