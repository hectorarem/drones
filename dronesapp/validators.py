import re
from django.core.exceptions import ValidationError


def validate_weight_limit(value):
    if 500 < value <= 0:
        raise ValidationError("Weight limit between 0.x and 500 gr")
    else:
        return value


def validate_weight(value):
    if value <= 0:
        raise ValidationError("Weight must be more than 0 gr")
    else:
        return value


def validate_battery_capacity(value):
    if 100 < value < 0:
        raise ValidationError("Battery percent between 0 and 100")
    else:
        return value


def validate_med_name(value):
    if re.match('^[a-zA-Z0-9_.-]*$', value):
        return value
    else:
        raise ValidationError("Allow only letters, numbers, '-', and '_'")


def validate_med_code(value):
    if re.match('^[A-Z0-9_]*$', value):
        return value
    else:
        raise ValidationError("Allow only upper case letters, underscore, and numbers")


def validate_image_size(value):
    if value.size > 204800:
        raise ValidationError("Image Max Size 2 MB. Please check your image")
    else:
        return value
