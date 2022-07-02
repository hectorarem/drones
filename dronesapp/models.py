import uuid
from django.db import models
from .validators import validate_weight, validate_weight_limit, validate_battery_capacity, validate_med_name, \
    validate_med_code, validate_image_size


class Drone(models.Model):
    MODEL_LIGHTWEIGHT = 'lightweight'
    MODEL_MIDDLEWEIGHT = 'middleweight'
    MODEL_CRUISERWEIGHT = 'cruiserweight'
    MODEL_HEAVYWEIGHT = 'heavyweight'
    MODELS = (
        (MODEL_LIGHTWEIGHT, 'Light weight'),
        (MODEL_MIDDLEWEIGHT, 'Middle weight'),
        (MODEL_CRUISERWEIGHT, 'Cruiser weight'),
        (MODEL_HEAVYWEIGHT, 'Heavy weight'),
    )
    STATE_IDLE = "idle"
    STATE_LOADING = "loading"
    STATE_LOADED = "loaded"
    STATE_DELIVERING = "delivering"
    STATE_DELIVERED = "delivered"
    STATE_RETURNING = "returning"
    STATES = (
        (STATE_IDLE, 'Idle'),
        (STATE_LOADING, 'loading'),
        (STATE_LOADED, 'loaded'),
        (STATE_DELIVERING, 'delivering'),
        (STATE_DELIVERED, 'delivered'),
        (STATE_RETURNING, 'returning'),
    )
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)
    serial_number = models.UUIDField(default=uuid.uuid4, editable=False)
    model = models.CharField('model', max_length=50, choices=MODELS)
    weight_limit_gr = models.FloatField('Weight Limit (gr)', validators=[validate_weight_limit])
    battery_capacity = models.IntegerField('Battery Capacity', validators=[validate_battery_capacity])
    state = models.CharField('state', max_length=50, choices=STATES)
    active = models.BooleanField('active', default=True)


    class Meta:
        verbose_name = 'drone'
        verbose_name_plural = 'drones'
        ordering = ('-created_at',)

    def __str__(self):
        return self.serial_number

    @property
    def enabled(self):
        return self.active and self.STATES == self.STATE_IDLE and self.battery_capacity >= 25

class Medication(models.Model):
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)
    name = models.CharField(max_length=255, validators=[validate_med_name])
    weight_gr = models.FloatField('Weight (gr)', validators=[validate_weight])
    code = models.CharField(max_length=255, validators=[validate_med_code])
    image = models.ImageField('image', upload_to="medication/", validators=[validate_image_size])

    class Meta:
        verbose_name = 'medication'
        verbose_name_plural = 'medications'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
