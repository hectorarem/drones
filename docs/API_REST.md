# API REST documentation.

For this project we have two types of documentation for the project endpoints and their interaction. One is the interface provided by the django rest framework, and the other is a collection of postams.

## Django Rest Framework UI

Django rest framework has a very friendly and helpful interface for developers, both backend and frontend. In other words, it is the mediator between both applications.

In our project we have two interfaces, one for the auth module, and another for the business module as such

### Auth endpoint

To access the auth endpoints(**1**), we must go to this address 

`http://127.0.0.1:8000/api/v1/auth/`

### Drone endpoints

To access the auth endpoints(**4**), we must go to this address 

`http://127.0.0.1:8000/api/v1/`

### How to interact with django rest framework?

This interface allows us to carry out the CRUD, in most cases, of the models that we have in the database. Perhaps at first it can become cumbersome to know the "how to do it", that's why we also have the POSTMAN documentation.

## Postman UI

First of all, the version of postman must be installed, which has its version for most operating systems
<a href="https://www.postman.com/"> See more </a>

Once we have our desktop application installed, we can import the Drones.postman_collections.json that we have in the root of the project.

### Structure

When importing the collection, we can see 5 folders, in which we have organized request examples of our REST API.

1. `auth` Have 3 endpoint for register, login and logout
2. `Drones` Have 7 examples of endpoint request, CRUD and how you can change state or battery charge only with `PATCH`
3. `Medication` have 4 examples of endpoint request, it is a CRUD.
4. `Battery Logs` Here we have 2 requests of the api, one is the complete list of logs, and the other, a filter that we have integrated specifying the drone_id, and the date range to display. 
5. `Drone-Med-Package` Here we have the list and the creation of a package to send.

### Note
The Authorization header must be sent at each endpoint.

If you want test without login required, you need comment
DEFAULT_PERMISSION_CLASSES in REST_FRAMEWORK dict in settings.py