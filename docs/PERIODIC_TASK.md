# Periodic task to check drones battery levels.

To solve this requirement, in a production environment and with servers, the solution may be, by example:
#### TECHNOLOGIES (docker, celery, django-celery-beat, redis)
0. Install docker.
1. Install Celery and django-celery-beat
2. Run on a Redis or RabbitMQ dockerized server or other options. Ex:

    `docker run -p 6379:6379 -d redis:5`
3. Configure the django application for celery.
4. Add migration for celery-beat and specify the frequency - time that we will consume the task

### In this project we are going to give a 'simple' solution, as it is a test, but trying to maintain the same philosophy that we have in a professional environment.

1. We will have a `task.py` file in which we will program the task of checking the batteries of all the drones and save it in the database.
2. We will have another file, `cronjobs.py`, which will do the task of the celery-beat, of calling the `update_drone_battery()` method every 1 minute
3. And finally we will make a command, which we will execute in another console, to start the process.

## How do we run the command?

1. Open a new console at the root of the project
2. Activate the environment(We already know how in the <a href="https://github.com/hectorarem/drones/blob/main/README.md">README.md</a>)
3. Run the command `python manage.py run_cron_jobs`
4. That's it.

