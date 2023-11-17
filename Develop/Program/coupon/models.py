from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from custom_user import models as customer_user_models


# Create your models here.
class Coupons(models.Model):
    class Meta:
        db_table = 'coupons'
        verbose_name_plural = 'coupons'

    # related fields
    custom_user_object = models.ForeignKey(customer_user_models.CustomUsers, on_delete=models.PROTECT)
    company_object = models.ForeignKey(customer_user_models.Companies, verbose_name='company', on_delete=models.PROTECT, null=False, blank=False)

    # normal fields
    coupon_name = models.CharField('coupon_name', max_length=255)
    description = models.TextField('description')
    started_on = models.DateField('started on', null=True, blank=True)
    finished_on = models.DateField('finished on', null=True, blank=True)
    max_number_of_sales = models.PositiveBigIntegerField("max number of sales", null=True, blank=True)
    show_sold_number = models.BooleanField(verbose_name='show sold number', default=True, help_text='If turn on this, User can see how many coupon sold.')

    regular_price = models.PositiveIntegerField('regular price')
    offer_price = models.PositiveIntegerField('offer price')

    address1 = models.CharField('adress1', help_text='Street name', max_length=255, null=True, blank=True)
    address2 = models.CharField('adress2', help_text='(Optional) building name', max_length=255, null=True, blank=True)
    city = models.CharField('city', help_text='or Town', max_length=255, null=True, blank=True)
    postal_code = models.CharField('postal code', max_length=255, null=True, blank=True)
    province = models.CharField('province', max_length=255, null=True, blank=True)
    country_object = models.ForeignKey(customer_user_models.Countries, verbose_name='country', on_delete=models.SET_NULL, null=True, blank=True)

class CouponImages(models.Model):
    coupon_object = models.ForeignKey(Coupons, on_delete=models.CASCADE)
    image = models.ImageField('images', upload_to='coupons/', null=False, blank=False)

class CouponReviews(models.Model):
    # related fields
    custom_user_object = models.ForeignKey(customer_user_models.CustomUsers, on_delete=models.PROTECT)
    coupon_object = models.ForeignKey(Coupons, on_delete=models.CASCADE)

    # normal fields
    rate = models.PositiveSmallIntegerField('rate', validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField('comment')
    created_on = models.DateField('created_on')

    
