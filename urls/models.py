from datetime import date

from django.db import models


class Url(models.Model):
    short_name = models.CharField(max_length=100)
    long_name = models.CharField(max_length=100, blank=None, null=None)
    popularity = models.IntegerField(blank=None, null=None)
    updated_date = models.DateField(default=date.today, blank=None, null=None)
