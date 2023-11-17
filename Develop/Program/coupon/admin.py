from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Coupons)
admin.site.register(models.CouponImages)
admin.site.register(models.CouponReviews)