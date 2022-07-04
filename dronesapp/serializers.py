from rest_framework import serializers
from .models import Drone, Medication, BatteryLogs, DronePackage


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

class DronePackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = DronePackage
        fields = ['drone', 'medications']

    def create(self, validated_data):
        total_weight = 0
        for m in validated_data['medications']:
            total_weight += m.weight_gr

        if validated_data['drone'].weight_limit_gr < total_weight:
            raise serializers.ValidationError({
                'msg': f"Error! Drone accept {validated_data['drone'].weight_limit_gr} gr and you are puting {total_weight} gr"
            })
        validated_data['weight_gr'] = total_weight
        return super().create(validated_data)

    def update(self, instance, validated_data):
        total_weight = 0
        for m in validated_data['medications']:
            total_weight += m.weight_gr

        if validated_data['drone'].weight_limit_gr < total_weight:
            raise serializers.ValidationError({
                'msg': f"Error! Drone accept {validated_data['drone'].weight_limit_gr} gr and you are puting {total_weight} gr"
            })
        validated_data['weight_gr'] = total_weight
        return super().update(instance, validated_data)



class ReadDronePackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = DronePackage
        fields = ['created_at', 'drone', 'medications', 'weight_gr', 'state', 'weight_left']
        depth = 1


class BatteryLogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BatteryLogs
        fields = ['check_at', 'drone', 'battery_level']
        depth = 1
