from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.viewsets import ModelViewSet
from .serializers import DroneSerializer, ReadDroneSerializer, MedicationSerializer, ReadMedicationSerializer, BatteryLogsSerializer
from .models import Drone, Medication, BatteryLogs

class DroneViewSet(ModelViewSet):

    serializer_class = DroneSerializer

    def get_queryset(self):
        queryset = Drone.objects.all()
        # filter = self.request.GET.get('filter', None)
        return queryset

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer_action_classes = {
            'list': ReadDroneSerializer,
            'create': DroneSerializer,
            'retrieve': ReadDroneSerializer,
            'update': DroneSerializer,
            'partial_update': DroneSerializer,
            'destroy': DroneSerializer
        }

    def get_serializer_class(self, *args, **kwargs):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()


class MedicationViewSet(ModelViewSet):

    serializer_class = MedicationSerializer

    def get_queryset(self):
        queryset = Medication.objects.all()
        # filter = self.request.GET.get('filter', None)
        return queryset

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer_action_classes = {
            'list': ReadMedicationSerializer,
            'create': MedicationSerializer,
            'retrieve': ReadMedicationSerializer,
            'update': MedicationSerializer,
            'partial_update': MedicationSerializer,
            'destroy': MedicationSerializer
        }

    def get_serializer_class(self, *args, **kwargs):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

class BatteryLogsViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = BatteryLogsSerializer

    def get_queryset(self):
        queryset = BatteryLogs.objects.all()
        drone_id = self.request.GET.get('drone_id', None)
        start_date = self.request.GET.get('start_date', None)
        end_date = self.request.GET.get('end_date', None)
        if drone_id:
            queryset = queryset.filter(drone_id=drone_id)
        if start_date:
            queryset = queryset.filter(check_at__gt=start_date)
        if end_date:
            queryset = queryset.filter(check_at__lt=end_date)
        return queryset


def home_render(request):
    return HttpResponseRedirect('/api/v1/')
