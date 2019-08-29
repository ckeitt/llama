# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.gis.db import models

from rider.models import Rider
from rider.models import Card

from vehicle.models import Vehicle

from pricing.models import Pricing

class Trip(models.Model):
    
    rider = models.ForeignKey(Rider, related_name='trips')
    card = models.ForeignKey(Card, related_name='+')
    vehicle = models.ForeignKey(Vehicle, related_name='trips')

    date_time_started = models.DateTimeField()
    date_time_ended = models.DateTimeField()

    seconds_driven = models.DecimalField(max_length=20, max_digits=20, decimal_places=10)
    pricing = models.ForeignKey(Pricing, related_name='+')

    activation_cost = models.DecimalField(max_length=10, max_digits=10, decimal_places=2)
    usage_cost = models.DecimalField(max_length=10, max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_length=10, max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_length=10, max_digits=10, decimal_places=2)

    active = models.BooleanField(default=False)
    
    path_traveled = models.LineStringField()
    miles_traveled = models.DecimalField(max_length=20, max_digits=20, decimal_places=10)
