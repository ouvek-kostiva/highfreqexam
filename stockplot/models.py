from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Twse(models.Model):
    indexcolumn = models.IntegerField(db_column='indexColumn', primary_key=True)  # Field name made lowercase.
    code = models.TextField()
    date = models.TextField()
    close = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'twse'