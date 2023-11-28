from django import forms

from . import models
from company import models as company_models

TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)

class CouponCreateForm(forms.ModelForm):
    company_object = forms.models.ModelChoiceField(company_models.Companies.objects.none(), label='Company')

    class Meta:
        model = models.Coupons
        exclude = ('custom_user_object', )
        widgets = {
            'started_on': forms.DateInput(format=('%m/%d/%Y'), attrs={'placeholder':'Select a date', 'type':'date'}),
            'finished_on': forms.DateInput(format=('%m/%d/%Y'), attrs={'placeholder':'Select a date', 'type':'date'}),            
            'show_sold_number': forms.Select(choices=TRUE_FALSE_CHOICES),
            'show_max_number_of_sales': forms.Select(choices=TRUE_FALSE_CHOICES),
        }

class CouponImageCreateForm(forms.ModelForm):
    class Meta:
        model = models.CouponImages
        fields = '__all__'
