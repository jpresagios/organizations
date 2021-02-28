# Organizations API

## To have installed:

- Python 3.X

  ```
  https://www.python.org/downloads/
  ```

## Install requirements

Create a Python Virtual enviroment, and change to the directory
requirements

For only development dependencies

```
pip install -r development.txt
```

For only production dependencies (In this case dependecies like django-debug-toolbar don't be installed)

```
pip install -r production.txt
```

## Enviroment

```
Create .env, please use  envsample content and change for your own
```

The variable DJANGO_SETTINGS_MODULE in .env defined the enviroment to run
the Project

For development

```
DJANGO_SETTINGS_MODULE=config.settings.development
```

For production

```
DJANGO_SETTINGS_MODULE=config.settings.production
```

## How to run app

```
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```

## Fixtures / Population initial data

This create initial auth groups **Administrator**, **Viewer**, **User**,
Organizations and Users Organizations (Members).<br>
One default user to test the API is

```
email = admin@admin.com
password = admin123
group = Administrator
```

For inserted additional data navigate to Django Admin. Model Organization, OrganizationMember (Reporesent the User Model) are register in Django Admin.

```
python manage.py initial_data
```

## How review API contracts documentation


```
python manage.py runserver
Navigate to /swagger
```


## How run tests

```
python manage.py test api
```

## Automation Build With Docker
Have docker and docker-compose in your computer

https://docs.docker.com/compose/install/
```
docker-compose up --build

The api is expose in http://localhost:8001/api
Navigate to http://localhost:8001/swagger/ to test everything work fine.
```


Docker start up process run everything to get the app ready to used. In
addition **initial_data** run to have some demo data for the purposes
of simple review this Task.

## Possible improvements
- Included an nginx to server the project, actually is running
using the develop django server inside Docker

- Covered with more tests the API, not everything was tested 