from django.db import migrations


def register_drones(apps, schema_editor):
    Drone = apps.get_model('dronesapp', 'Drone')
    # 1
    Drone.objects.get_or_create(
        model='lightweight',
        weight_limit_gr=40,
        battery_capacity=100,
        state='idle',
    )
    # 2
    Drone.objects.get_or_create(
        model='lightweight',
        weight_limit_gr=50,
        battery_capacity=100,
        state='idle',
    )
    # 3
    Drone.objects.get_or_create(
        model='middleweight',
        weight_limit_gr=120,
        battery_capacity=100,
        state='idle',
    )
    # 4
    Drone.objects.get_or_create(
        model='middleweight',
        weight_limit_gr=150,
        battery_capacity=100,
        state='idle',
    )
    # 5
    Drone.objects.get_or_create(
        model='cruiserweight',
        weight_limit_gr=200,
        battery_capacity=100,
        state='idle',
    )
    # 6
    Drone.objects.get_or_create(
        model='cruiserweight',
        weight_limit_gr=200,
        battery_capacity=100,
        state='idle',
    )
    # 7
    Drone.objects.get_or_create(
        model='cruiserweight',
        weight_limit_gr=250,
        battery_capacity=100,
        state='idle',
    )
    # 8
    Drone.objects.get_or_create(
        model='heavyweight',
        weight_limit_gr=380,
        battery_capacity=100,
        state='idle',
    )
    # 9
    Drone.objects.get_or_create(
        model='heavyweight',
        weight_limit_gr=450,
        battery_capacity=100,
        state='idle',
    )
    # 10
    Drone.objects.get_or_create(
        model='heavyweight',
        weight_limit_gr=500,
        battery_capacity=100,
        state='idle',
    )



def remove_drones(apps, schema_editor):
    Drone = apps.get_model('dronesapp', 'Drone')
    Drone.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('dronesapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(register_drones, remove_drones),
    ]
