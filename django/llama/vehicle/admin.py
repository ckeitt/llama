# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from vehicle.models import Vehicle
from vehicle.models import VehicleType

admin.site.register(Vehicle)
admin.site.register(VehicleType)
