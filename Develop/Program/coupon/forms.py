from django import forms

from . import models
from custom_user import models as user_models

TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)

class CouponCreateForm(forms.ModelForm):
    company_object = forms.models.ModelChoiceField(user_models.Companies.objects.none(), label='Company')

    class Meta:
        model = models.Coupons
        exclude = ('custom_user_object', )
        widgets = {
            'started_on': forms.DateInput(format=('%m/%d/%Y'), attrs={'placeholder':'Select a date', 'type':'date'}),
            'finished_on': forms.DateInput(format=('%m/%d/%Y'), attrs={'placeholder':'Select a date', 'type':'date'}),            
            'show_sold_number': forms.Select(choices=TRUE_FALSE_CHOICES),
        }

coupon_image_forms = forms.inlineformset_factory(
    parent_model=models.Coupons,
    model=models.CouponImages,
    fields=('image', ),
    extra=10,
)