from django.db import models
from .model_publisher import Publisher

class Supplier(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=100)
    suburb = models.CharField(max_length=100)
    city = models.CharField(max_length=80)
    country = models.CharField(max_Length=80)
    website = models.URLField()
    publishers = models.ManyToManyField(Publisher)

    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'supplier'
        app_label = 'patm'