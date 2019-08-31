from django.conf.urls import url
from vehicle import views as vehicle_views

urlpatterns = [
    url(r'^vehicle/unlock$', vehicle_views.UnlockVehicleView.as_view()),
]
