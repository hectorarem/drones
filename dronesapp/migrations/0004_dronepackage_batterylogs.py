# Generated by Django 4.0.4 on 2022-07-04 01:54

from django.db import migrations, models
import django.db.models.deletion
import dronesapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('dronesapp', '0003_seeds_medications'),
    ]

    operations = [
        migrations.CreateModel(
            name='DronePackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('weight_gr', models.FloatField(validators=[dronesapp.validators.validate_weight], verbose_name='Weight (gr)')),
                ('drone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dronesapp.drone', verbose_name='drone')),
                ('medications', models.ManyToManyField(to='dronesapp.medication', verbose_name='medications')),
            ],
            options={
                'verbose_name': 'drone package',
                'verbose_name_plural': 'drone packages',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='BatteryLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_at', models.DateTimeField(auto_now_add=True, verbose_name='check at')),
                ('battery_level', models.FloatField(validators=[dronesapp.validators.validate_battery_capacity], verbose_name='battery level')),
                ('drone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dronesapp.drone', verbose_name='drone')),
            ],
            options={
                'verbose_name': 'battery log',
                'verbose_name_plural': 'battery logs',
                'ordering': ('-check_at',),
            },
        ),
    ]
