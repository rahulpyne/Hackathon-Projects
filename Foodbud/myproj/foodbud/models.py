from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Meals(models.Model):
    item_id = models.CharField(max_length=50,null =True)
    brand_id = models.CharField(max_length=50, null = True)
    brand_name = models.CharField(max_length=37,null = True)
    item_name = models.CharField(max_length=80,null = True)
    price = models.FloatField()
    category = models.CharField(max_length=7,null = True)
    item_description=models.TextField(null = True)
    calories = models.FloatField(null = True)


def __str__(self):
    return unicode(self).encode('utf-8')
