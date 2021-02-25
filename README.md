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

## How review API contracts documentation

```
python manage.py runserver
Navigate to /swagger
```
