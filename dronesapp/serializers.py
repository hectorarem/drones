from rest_framework import serializers
from .models import Drone, Medication


class DroneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drone
        fields = ['model', 'weight_limit_gr', 'battery_capacity', 'state', 'active']


class ReadDroneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drone
        fields = ['created_at', 'updated_at', 'serial_number', 'model', 'weight_limit_gr',
                  'battery_capacity', 'state', 'active', 'enabled']

class MedicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medication
        fields = ['name', 'weight_gr', 'code', 'image']


class ReadMedicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medication
        fields = ['created_at', 'updated_at', 'name', 'weight_gr', 'code', 'image']

