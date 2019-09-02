# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from llama import settings
from django.contrib.gis.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save

class VehicleType(models.Model):
        
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    thumbnail_image = models.ImageField(upload_to='vehicles/thumnail_images', blank=True)
    marketing_image = models.ImageField(upload_to='vehicles/thumnail_images', blank=True)

    max_daily_battery_usage = models.DecimalField(max_length=10, max_digits=10, decimal_places=2)
    
    def __unicode__(self):
        return self.name

class Vehicle(models.Model):
        
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    access_key = models.CharField(max_length=255, blank=True, null=True)
    qr_verification_code = models.CharField(max_length=255, blank=True, null=True)

    public_ip_address = models.CharField(max_length=255, blank=True, null=True)
    port_number = models.CharField(max_length=255, blank=True, null=True)

    battery_percentage = models.DecimalField(max_length=10, max_digits=10, decimal_places=5)

    current_location = models.PointField(blank=True, null=True)

    vehicle_type = models.ForeignKey(VehicleType, related_name='+', blank=True, null=True)
    
    def __unicode__(self):
        return self.name

@receiver(post_save, sender=Vehicle)
def assignValidationCodes(sender, instance, created, **kwargs):
    if (created):
        
        random_qr = random.randint(10**(settings.QR_CODE_LENGTH-1), (10**settings.QR_CODE_LENGTH)-1)

        while (Vehicle.objects.filter(qr_verification_code=random_qr).count() > 0):
            random_qr = random.randint(10**(settings.QR_CODE_LENGTH-1), (10**settings.QR_CODE_LENGTH)-1)

        random_access_key = random.randint(10**(settings.VALIDATION_CODE_LENGTH-1), (10**settings.VALIDATION_CODE_LENGTH)-1)

        while (Vehicle.objects.filter(access_key=random_access_key).count() > 0):
            random_access_key = random.randint(10**(settings.VALIDATION_CODE_LENGTH-1), (10**settings.VALIDATION_CODE_LENGTH)-1)

        instance.qr_verification_code = random_qr
        instance.access_key = random_access_key
        instance.save()
