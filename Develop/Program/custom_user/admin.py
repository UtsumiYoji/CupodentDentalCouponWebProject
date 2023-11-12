from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Countries)
admin.site.register(models.CustomUsers)
admin.site.register(models.Companies)