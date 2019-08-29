# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.gis.db import models

from phonenumber_field.modelfields import PhoneNumberField

class Card(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cards')

    object = models.CharField(max_length=255, null=True, blank=True)
    address_city = models.CharField(max_length=255, null=True, blank=True)
    address_country = models.CharField(max_length=255, null=True, blank=True)
    address_line1 = models.CharField(max_length=255, null=True, blank=True)
    address_line1_check = models.CharField(max_length=255, null=True, blank=True)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)
    address_state = models.CharField(max_length=255, null=True, blank=True)
    address_zip = models.CharField(max_length=255, null=True, blank=True)
    address_zip_check = models.CharField(max_length=255, null=True, blank=True)

    brand = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    cvc_check = models.CharField(max_length=255, null=True, blank=True)

    dynamic_last4 = models.CharField(max_length=255, null=True, blank=True)

    exp_month = models.CharField(max_length=255, null=True, blank=True)
    exp_year = models.CharField(max_length=255, null=True, blank=True)
    funding = models.CharField(max_length=255, null=True, blank=True)
    last4 = models.CharField(max_length=255, null=True, blank=True)

    fingerprint = models.CharField(max_length=255, null=True, blank=True)
    metadata = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    tokenization_method = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=False)
    
    def __unicode__(self):
        if (self.id):
            return self.id
        else:
            return '%s' % self.last4

class DriversLicense(models.Model):

    rider = models.OneToOneField('Rider', related_name='license')
    image = models.ImageField(upload_to='riders/licenses', blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    issuance_date = models.DateTimeField(null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    license_number = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        if (self.rider.user.first_name and self.rider.user.last_name):
            return '%s %s - %s' % (self.rider.user.first_name, self.rider.user.last_name)

class Rider(models.Model):
        
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rider')

    device_id = models.CharField(max_length=255, blank=True, null=True)
    verified_email = models.BooleanField(default=False)

    profile_photo = models.ImageField(upload_to='riders/profile_photos', blank=True)
    current_location = models.PointField(blank=True, null=True)

    phone_number = PhoneNumberField(blank=True, null=True)
    verified_phone_number = models.BooleanField(default=False)

    stripe_account_id = models.CharField(max_length=255, blank=True, null=True)
    referral_code = models.CharField(max_length=244, blank=True, null=True)
    
    def __unicode__(self):
        return self.user.email_address

class StripeUser(models.Model):

    id = models.CharField(max_length=255, primary_key=True)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='stripe_user')
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
