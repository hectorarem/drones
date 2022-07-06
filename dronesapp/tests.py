import base64

from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from .models import Drone, Medication, DronePackage
from io import BytesIO
from PIL import Image

c = Client()


class DroneTestCase(TestCase):
    api = '/api/v1/'
    user_login = {"username": "man", "password": "zaqwsxcde123/*-+"}
    api_auth = f"{api}auth/"
    api_drones = f"{api}drone/"
    api_medication = f"{api}medication/"
    api_drone_package = f"{api}drone-package/"
    api_battery_logs = f"{api}battery-logs/"

    def setUp(self):
        User.objects.create_user(username="man", email='man@gmail.com', password='zaqwsxcde123/*-+')

    def login(self):
        """login"""
        response = c.post(f'{self.api_auth}login', self.user_login)
        return response.json()

    def test_battery_logs_list(self):
        login = self.login()
        if login['access']:
            access = login['access']
            bearer = f"Bearer {access}"
            list = c.get(self.api_battery_logs, HTTP_AUTHORIZATION=bearer)
            self.assertEqual(list.status_code, 200)

    def test_drones_crud(self):
        login = self.login()
        if login['access']:
            access = login['access']
            user_id = login['user']['id']
            bearer = f"Bearer {access}"

            # we have already 9 drones in our system thanks drone migrations
            drone_count = Drone.objects.count()

            #CREATE
            data = {
                "model": Drone.MODEL_LIGHTWEIGHT,
                "weight_limit_gr": 50,
                "battery_capacity": 97,
                "state": Drone.STATE_IDLE
            }
            new_drone = c.post(self.api_drones, data=data, HTTP_AUTHORIZATION=bearer)
            self.assertEqual(new_drone.status_code, 201)

            # confirm create
            self.assertEqual(Drone.objects.count(), drone_count + 1)

            last_drone = Drone.objects.last()

            # Read
            read_drone = c.get(f'{self.api_drones}{last_drone.pk}/', HTTP_AUTHORIZATION=bearer)
            self.assertEqual(read_drone.status_code, 200)

            # Update
            data = {
                "model": Drone.MODEL_CRUISERWEIGHT,
                "weight_limit_gr": 200,
                "battery_capacity": 80,
                "state": Drone.STATE_IDLE
            }

            drone_update = c.put(f'{self.api_drones}{last_drone.pk}/', data=data, HTTP_AUTHORIZATION=bearer, content_type='application/json')
            self.assertEqual(drone_update.status_code, 200)

            # Check if name change
            updated_drone = Drone.objects.get(pk=last_drone.pk)
            self.assertNotEqual(last_drone.battery_capacity, updated_drone.battery_capacity)

            # Delete
            delete_drone = c.delete(f'{self.api_drones}{last_drone.pk}/', HTTP_AUTHORIZATION=bearer)
            self.assertEqual(delete_drone.status_code, 204)
            # confirm delete
            self.assertEqual(Drone.objects.count(), drone_count)

    def test_medication_crud(self):
        login = self.login()
        if login['access']:
            access = login['access']
            bearer = f"Bearer {access}"

            # we have already 10 meidcations in our system thanks drone migrations
            med_count = Medication.objects.count()

            #CREATE
            data = {
                "name": "name_example123",
                "weight_gr": 10,
                "code": "NE123",
            }
            new_med = c.post(self.api_medication, data=data, HTTP_AUTHORIZATION=bearer)
            self.assertEqual(new_med.status_code, 201)

            # confirm create
            self.assertEqual(Medication.objects.count(), med_count + 1)

            last_med = Medication.objects.last()

            # Read
            read_med = c.get(f'{self.api_medication}{last_med.pk}/', HTTP_AUTHORIZATION=bearer)
            self.assertEqual(read_med.status_code, 200)

            # Update
            data = {
                "name": "name_example321",
                "weight_gr": 50,
                "code": "NE321",
            }

            med_update = c.put(f'{self.api_medication}{last_med.pk}/', data=data, HTTP_AUTHORIZATION=bearer, content_type='application/json')
            self.assertEqual(med_update.status_code, 200)

            # Check if name change
            updated_med = Medication.objects.get(pk=last_med.pk)
            self.assertNotEqual(last_med.name, updated_med.name)

            # Delete
            delete_med = c.delete(f'{self.api_medication}{last_med.pk}/', HTTP_AUTHORIZATION=bearer)
            self.assertEqual(delete_med.status_code, 204)
            # confirm delete
            self.assertEqual(Medication.objects.count(), med_count)

    def test_drone_package(self):
        login = self.login()
        if login['access']:
            access = login['access']
            bearer = f"Bearer {access}"

            # CREATE
            data = {
                "drone": "8",
                "medications": [1, 2, 3],
            }
            new_drone_package = c.post(self.api_drone_package, data=data, HTTP_AUTHORIZATION=bearer, content_type='application/json')
            self.assertEqual(new_drone_package.status_code, 201)

            # confirm create
            self.assertEqual(DronePackage.objects.count(), 1)

            last_drone_package = DronePackage.objects.last()

            # Read
            read_drone_package = c.get(f'{self.api_drone_package}{last_drone_package.pk}/', HTTP_AUTHORIZATION=bearer)
            self.assertEqual(read_drone_package.status_code, 200)

            # Update
            data = {
                "drone": "8",
                "medications": [4, 5, 6],
            }

            update_drone_package = c.put(f'{self.api_drone_package}{last_drone_package.pk}/', data=data, HTTP_AUTHORIZATION=bearer,
                               content_type='application/json')
            self.assertEqual(update_drone_package.status_code, 200)

            # Check if package change
            updated_drone_package = DronePackage.objects.get(pk=last_drone_package.pk)
            self.assertNotEqual(last_drone_package.weight_left, updated_drone_package.weight_left)

            # Delete
            delete_drone_package = c.delete(f'{self.api_drone_package}{last_drone_package.pk}/', HTTP_AUTHORIZATION=bearer)
            self.assertEqual(delete_drone_package.status_code, 204)
            # confirm delete
            self.assertEqual(DronePackage.objects.count(), 0)

    def test_drone_package_limit(self):
        login = self.login()
        if login['access']:
            access = login['access']
            bearer = f"Bearer {access}"

            # CREATE
            data = {
                "drone": "8",
                "medications": [1, 2, 3, 4, 5, 6],
            }
            new_drone_package = c.post(self.api_drone_package, data=data, HTTP_AUTHORIZATION=bearer, content_type='application/json')
            # Example response {'msg': 'Error! Drone accept 450.0 gr and you are puting 603.0 gr'}
            self.assertEqual(new_drone_package.status_code, 400)

    def test_drones_form_validations(self):
        login = self.login()
        if login['access']:
            access = login['access']
            bearer = f"Bearer {access}"

            # percent validation
            data = {
                "model": Drone.MODEL_LIGHTWEIGHT,
                "weight_limit_gr": 50,
                "battery_capacity": 197,
                "state": Drone.STATE_IDLE
            }
            new_drone = c.post(self.api_drones, data=data, HTTP_AUTHORIZATION=bearer)
            # Example response {'battery_capacity': ['Battery percent between 0 and 100']}
            self.assertEqual(new_drone.status_code, 400)

            # weight and - percent validation
            data = {
                "model": Drone.MODEL_LIGHTWEIGHT,
                "weight_limit_gr": 1000,
                "battery_capacity": -95,
                "state": Drone.STATE_IDLE
            }
            new_drone = c.post(self.api_drones, data=data, HTTP_AUTHORIZATION=bearer)
            # Example response {'weight_limit_gr': ['Weight limit between 0.x and 500 gr'], 'battery_capacity': ['Battery percent between 0 and 100']}
            self.assertEqual(new_drone.status_code, 400)

    def test_medication_form_validation(self):
        login = self.login()
        if login['access']:
            access = login['access']
            bearer = f"Bearer {access}"

            # Name Validation
            data = {
                "name": "name example123",
                "weight_gr": 10,
                "code": "NE123",
            }
            new_med = c.post(self.api_medication, data=data, HTTP_AUTHORIZATION=bearer)
            # Example response {'name': ["Allow only letters, numbers, '-', and '_'"]}
            self.assertEqual(new_med.status_code, 400)

            # code Validation
            data = {
                "name": "name-example123",
                "weight_gr": 10,
                "code": "NEa123",
            }
            new_med = c.post(self.api_medication, data=data, HTTP_AUTHORIZATION=bearer)
            # Example response 'code': ['Allow only upper case letters, underscore, and numbers']}
            self.assertEqual(new_med.status_code, 400)

