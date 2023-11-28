from django.db import models

# Create your models here.
class Countries(models.Model):
    class Meta:
        db_table = 'countries'
        verbose_name_plural = 'countries'
    
    def __str__(self) -> str:
        return self.name

    name = models.CharField('name', max_length=255, null=False, blank=False)