# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.gis.db import models

from rider.models import Rider

from vehicle.models import VehicleType

class Country(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True)
    abbreviated_name = models.CharField(max_length=255, blank=True, null=True)
    area = models.PolygonField()

    def __unicode__(self):
        return self.name

class State(models.Model):
    
    name = models.CharField(max_length=255, blank=True, null=True)
    abbreviated_name = models.CharField(max_length=255, blank=True, null=True)
    area = models.PolygonField()
    country = models.ForeignKey(Country, related_name='states')

    def __unicode__(self):
        return self.name

class Market(models.Model):
    
    name = models.CharField(max_length=255, blank=True, null=True)
    area = models.PolygonField()
    state = models.ForeignKey(Country, related_name='markets')

    def __unicode__(self):
        return self.name

class District(models.Model):
    
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    area = models.PolygonField()
    market = models.ForeignKey(Country, related_name='districts')

    def __unicode__(self):
        return self.name

class Pricing(models.Model):
    
    activation_fee = models.DecimalField(max_length=10, max_digits=10, decimal_places=4)
    usage_fee = models.DecimalField(max_length=10, max_digits=10, decimal_places=4)
    district = models.ForeignKey(District, related_name='+', blank=True, null=True)
    market = models.ForeignKey(Market, related_name='+', blank=True, null=True)
    state = models.ForeignKey(State, related_name='+', blank=True, null=True)
    country = models.ForeignKey(Country, related_name='+', blank=True, null=True)
    vehicle_type = models.ForeignKey(VehicleType, related_name='pricing')

    def __unicode__(self):
        return self.vehicle_type.name

class Credit(models.Model):

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    discount_dollar_type = models.BooleanField(default=True)
    discount_percentage_type = models.BooleanField(default=False)

    discount = models.DecimalField(max_length=10, max_digits=10, decimal_places=2, default=0)
    discount_percentage = models.DecimalField(max_length=10, max_digits=10, decimal_places=5, default=0)

    def __unicode__(self):
        return self.title

class PromotionalCredit(models.Model):

    credit = models.ForeignKey(Credit)
    active = models.BooleanField(default=True)
    code = models.CharField(max_length=255)
    max_number_of_uses = models.IntegerField(default=1)

    def __unicode__(self):
        return self.credit.title

class RiderPromotionalCredit(models.Model):

    promotion = models.ForeignKey(PromotionalCredit)
    rider = models.ForeignKey(Rider, null=True, blank=True, related_name='promotions')

    number_of_times_used = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s, %s' % (self.promotion.credit.title, self.rider.user.email_address)

class RiderCredit(models.Model):

    rider = models.ForeignKey(Rider, null=True, blank=True, related_name='credits')
    referring_rider = models.ForeignKey(Rider, null=True, blank=True, related_name='referring_credits')

    code = models.CharField(max_length=255, null=True, blank=True)
    
    rider_credit = models.ForeignKey(Credit, null=True, blank=True, related_name='+')
    referring_rider_credit = models.ForeignKey(Credit, null=True, blank=True, related_name='+')
    
    days_available_type = models.BooleanField(default=False)
    usage_number_type = models.BooleanField(default=True)

    max_days_available = models.IntegerField(default=1)
    max_number_of_uses = models.IntegerField(default=1)
    
    rider_amount_used = models.DecimalField(max_length=10, max_digits=10, decimal_places=2, default=0)
    referring_rider_amount_used = models.DecimalField(max_length=10, max_digits=10, decimal_places=2, default=0)

    def __unicode__(self):
        return self.rider.user.email_address
