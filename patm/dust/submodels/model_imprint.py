from django.db import models
from .model_publisher import Publisher

class Imprint(models.Model):
    name = models.CharField(max_length=80)
    publisher = models.ForeignKey(Publisher)
    website = models.URLField()

    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'publisher'
        app_label = 'patm'