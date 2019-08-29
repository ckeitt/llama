# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from rider.models import Rider
from rider.models import Card
from rider.models import DriversLicense
from rider.models import StripeUser

admin.site.register(Rider)
admin.site.register(Card)
admin.site.register(DriversLicense)
admin.site.register(StripeUser)
