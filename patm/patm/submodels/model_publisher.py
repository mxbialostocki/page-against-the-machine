from django.db import models
from .model_imprint import Imprint

class Publisher(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=100)
    suburb = models.CharField(max_length=100)
    city = models.CharField(max_length=80)
    country = models.CharField(max_Length=80)
    website = models.URLField()
    imprints = models.ManyToManyField(Imprint)

    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'publisher'
        app_label = 'patm'