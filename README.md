# Drones
We have a fleet of **10 drones**. A drone is capable of carrying devices, other than cameras, and capable of delivering small loads. For our use case **the load is medications**.

### Technologies
1. Python >= `3.7` (local uses `3.9`)
2. Django `4.0.4`
3. Django Rest Framework `3.13.x`
4. You can see more <a href="https://github.com/hectorarem/drones/blob/main/requirements.txt">here</a>

## First steps

1. Create a new virtual environment:

        python3 -m venv venv

2. Activate the environment:

        source venv/bin/activate

3. The environment has to be activated for the rest of the commands.

4. Install dependencies:

        pip install -r requirements.txt

5. Initialize the database:

        python manage.py migrate

6. Create superuser:

        python manage.py createsuperuser
        
   user created
        
        user:musala password:software2020/*-+

7. Start the development server:

        python manage.py runserver

### Unit Test
System endpoints are tested. Each test is unitary for each application.

Tested functionalities and project requirements.
1. login
2. logout
3. user registration
4. Drone CRUD
5. Medication CRUD
6. Drone medication Package CRUD
7. Battery Logs List
8. Drone medication package limit (500 gr)
9. Drone form validations
10. Medication form validations

You can run in the project's root
        
     python manage.py test
        
## For API Rest documentation, visit this doc for info
<a href="https://github.com/hectorarem/drones/blob/main/docs/API_REST.md">API REST DOCs</a>
        
## For periodic task, visit this doc for info.

<a href="https://github.com/hectorarem/drones/blob/main/docs/PERIODIC_TASK.md">PERIODIC TASK DOCs</a>