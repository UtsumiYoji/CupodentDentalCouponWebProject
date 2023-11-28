from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import Countries

# Create your models here.
class Companies(models.Model):
    class Meta:
        db_table = 'companies'
        verbose_name_plural = 'companies'
        
    name = models.CharField('company name', max_length=255, null=False, blank=False)
    _phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField('phone number', validators=[_phone_regex], max_length=17, blank=False, null=False)
    email = models.EmailField(_("email address"), blank=False, null=False)
    address1 = models.CharField('adress1', help_text='Street name', max_length=255, null=False, blank=False)
    address2 = models.CharField('adress2', help_text='(Optional) building name', max_length=255, null=True, blank=True)
    city = models.CharField('city', help_text='or Town', max_length=255, null=False, blank=False)
    postal_code = models.CharField('postal code', max_length=255, null=False, blank=False)
    province = models.CharField('province', max_length=255, null=False, blank=False)
    country_object = models.ForeignKey(Countries, verbose_name='country', on_delete=models.SET_NULL, null=True)
    image = models.ImageField('comapny logo', upload_to='comapanies/', null=False, blank=False)
    approved = models.BooleanField('approved', default=False, null=False, blank=False)

    def __str__(self) -> str:
        return self.name