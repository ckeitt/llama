# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.shortcuts import render

from rest_framework import status

from vehicle.models import Vehicle
from vehicle.manager import VehicleSocketManager

class UnlockVehicleView(generics.GenericAPIView):
    """
    View to allow registered users to unlock the vehicle based on the scanned QR code.

    * Public availability to all registered users.
    """

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        qr_code = request.data.pop('qr_verification_code')
        vehicle = Vehicle.objects.get(qr_verification_code=qr_code)
        socket_manager = VehicleSocketManager(vehicle.public_ip_address, vehicle.port_number, vehicle.access_key)
        socket_manager.unlock_vehicle()
        
        return Response(data={'vehicle_status' : 'unlocked'}, status=status.HTTP_200_OK)
