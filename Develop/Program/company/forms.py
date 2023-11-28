from django import forms

from . import models

class CreateForm(forms.ModelForm):
    class Meta:
        model = models.Companies
        exclude = ('approved', )