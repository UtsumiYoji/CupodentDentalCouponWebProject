from django import forms

from . import models

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = models.CustomUsers
        exclude = (
            'last_login', 'is_active', 'is_staff', 'date_joined', 
            'is_superuser', 'groups', 'user_permissions',
            'business_account', 'company', 'username')