from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'drone', views.DroneViewSet, basename='drone')
router.register(r'medication', views.MedicationViewSet, basename='medication')

urlpatterns = [
    path('', include(router.urls)),
]