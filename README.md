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

This create initial auth groups Administrator, Viewer, User
Different organizations and users
At least one known user to test the API that you can used after this command executed is
email = admin@admin.com
password = admin123
group = Administrator

For inserted additional data navigate to Django Admin

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

## Databases

Change the .env variable for your database, this project was tested so far
with sqlite and Postgresql.

You can use the variable **DATABASE_URL** in the .env
to specify the database, by default envsample sample is
DATABASE_URL=sqlite:///db.organization.db
but you can used PostgreSQL if you installed it in your machine,
sample database url for PostgreSQL postgres://<youruser>:<yourpassword>@localhost/db_organizations
