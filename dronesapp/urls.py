from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'drone', views.DroneViewSet, basename='drone')
router.register(r'medication', views.MedicationViewSet, basename='medication')
router.register(r'drone-package', views.DronePackageViewSet, basename='drone-package')
router.register(r'battery-logs', views.BatteryLogsViewSet, basename='battery-logs')

urlpatterns = [
    path('', include(router.urls)),
]