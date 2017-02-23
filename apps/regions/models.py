from __future__ import unicode_literals

from django.db import models

from ..game_of_thrones.models import House

# Create your models here.


class Region(models.Model):
    name = models.CharField(max_length=200)
    houses = models.ForeignKey(House, related_name="home_region", null=True)
    climate = models.CharField(max_length=200)
    known_for = models.CharField(max_length=200)
    #adjacent_region
