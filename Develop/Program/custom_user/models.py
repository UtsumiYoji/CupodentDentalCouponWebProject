from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Countries(models.Model):
    class Meta:
        db_table = 'countries'
        verbose_name_plural = 'countries'
    
    def __str__(self) -> str:
        return self.name

    name = models.CharField('name', max_length=255, null=False, blank=False)

class Companies(models.Model):
    class Meta:
        db_table = 'companies'
        verbose_name_plural = 'companies'
        
    name = models.TextField('name', null=False, blank=False)
    _phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField('phone number', validators=[_phone_regex], max_length=17, blank=True)
    address1 = models.TextField('adress1', help_text='Street name', null=False, blank=False)
    address2 = models.TextField('adress2', help_text='Optional, building name', null=False, blank=False)
    city = models.CharField('city', help_text='or Town', max_length=255, null=False, blank=False)
    postal_code = models.CharField('postal code', max_length=255, null=False, blank=False)
    province = models.CharField('province', max_length=255, null=False, blank=False)
    country = models.ForeignKey(Countries, on_delete=models.SET_NULL, null=True)

GENDER = (('male', 'male'), ('female', 'female'), ('other', 'other'))
class CustomUsers(AbstractUser):
    email = models.EmailField(("email address"), blank=False, null=False)

    business_account = models.BooleanField('business account', default=False, null=False, blank=False)
    gender = models.CharField('gender', max_length=20, choices=GENDER, null=False, blank=False)
    _phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField('phone number', validators=[_phone_regex], max_length=17, blank=True, null=True)
    address1 = models.CharField('adress1', help_text='Street name', max_length=255, null=True, blank=True)
    address2 = models.CharField('adress2', help_text='(Optional) building name', max_length=255, null=True, blank=True)
    city = models.CharField('city', help_text='or Town', max_length=255, null=True, blank=True)
    postal_code = models.CharField('postal code', max_length=255, null=True, blank=True)
    province = models.CharField('province', max_length=255, null=True, blank=True)
    country = models.ForeignKey(Countries, on_delete=models.SET_NULL, null=True)
    company = models.ManyToManyField(Companies, blank=True)
