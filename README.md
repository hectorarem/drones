# Drones
We have a fleet of **10 drones**. A drone is capable of carrying devices, other than cameras, and capable of delivering small loads. For our use case **the load is medications**.

1. Create a new virtual environment:

        python3 -m venv env

2. Activate the environment:

        source env/bin/activate

3. The environment has to be activated for the rest of the commands.

4. Install dependencies:

        pip install -r requirements.txt

5. Initialize the database:

        python manage.py migrate

6. Create superuser:

        python manage.py createsuperuser

7. Start the development server:

        python manage.py runserver
        
## For periodic task, visit this doc for more info.

<a href="https://github.com/hectorarem/drones/blob/main/docs/PERIODIC_TASK.md">PERIODIC_TASK</a>