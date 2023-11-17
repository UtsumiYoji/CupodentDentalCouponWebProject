from django.contrib.auth import forms as auth_forms

from . import models

class UserCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = models.CustomUsers
        fields = (
            'email', 'gender', 'phone_number', 
            'address1', 'address2', 'city', 'postal_code',
            'province', 'country_object', 'first_name', 'last_name'
        )

class UserChangeForm(auth_forms.UserChangeForm):
    class Meta:
        model = models.CustomUsers
        fields = (
            'email', 'gender', 'phone_number', 
            'address1', 'address2', 'city', 'postal_code',
            'province', 'country_object', 'first_name', 'last_name'
        )