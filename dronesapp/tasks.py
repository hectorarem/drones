from .models import BatteryLogs, Drone
# from celery import shared_task


# @shared_task
def update_drone_battery():
    for drone in Drone.objects.filter(active=True):
        BatteryLogs.objects.create(drone=drone, battery_level=drone.battery_capacity)
