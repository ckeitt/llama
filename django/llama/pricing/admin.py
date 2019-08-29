# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from pricing.models import Country
from pricing.models import State
from pricing.models import Market
from pricing.models import District
from pricing.models import Pricing
from pricing.models import Credit
from pricing.models import PromotionalCredit
from pricing.models import RiderPromotionalCredit
from pricing.models import RiderCredit

admin.site.register(Country)
admin.site.register(State)
admin.site.register(Market)
admin.site.register(District)
admin.site.register(Pricing)
admin.site.register(Credit)
admin.site.register(PromotionalCredit)
admin.site.register(RiderPromotionalCredit)
admin.site.register(RiderCredit)
