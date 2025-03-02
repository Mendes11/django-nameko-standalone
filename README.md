
**This Project has been Forked due to the original being discontinued** 

# DJANGO NAMEKO STANDALONE
[![PyPI version](https://badge.fury.io/py/nameko-django-orm.svg)](https://badge.fury.io/py/nameko-django-orm) 
[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/nameko-django-orm.svg)](https://pypi.python.org/pypi/nameko-django-orm/)
[![Build Status](https://github.com/mendes11/django-nameko-standalone/actions/workflows/check.yml/badge.svg)](https://github.com/mendes11/django-nameko-standalone/actions/workflows/check.yml)

## Use django into your nameko services
## Requirements
Developed for Python3.8.

Have dependecies of:

* Django==3.0.7
* nameko==3.0.0-rc11

## Installation
`pip install nameko-django-orm`

## Usage
This package setup the django framework to take advantage of the ORM features and some other django features.

`DjangoModels` will load all your apps models into one single space where the models are exposed.

If you have your models into`app1.models` and `app2.models`, your app models will be exposed from one point at your election (i.e. `models` or whatever other variable you inject `DjangoModels`).

You need to specify the DJANGO_NAMEKO_STANDALONE_SETTINGS_MODULE or DJANGO_SETTINGS_MODULE environment variable, if not, a 'settings' file is used by default.

Inject the dependency into the nameko service with the DjangoModels dependency.

Supposing you injected the DjangoModels dependency into the `models` variable, you can use from your procedures like `self.models.MyModel.objects.all()`.


## Configuration
### Django nameko standalone configuration
django-nameko-standalone need the next settings variable to work:
```python
# MANDATORY
DJANGO_NAMEKO_STANDALONE_APPS = ("<my_django_app>",)

# OPTIONAL
DJANGO_NAMEKO_STANDALONE_SETTINGS_MODULE = 'my_settings'

# OPTIONAL | DEFAULT
DJANGO_SETTINGS_MODULE = "my_settings"
```
This variable control the applications where to load models.


### Django configuration
To configure the django ORM, just configure it as normally for Django.

The `INSTALLED_APPS` and `SECRET_KEY` settings needs to be defined to make Django work.

```python
# Minimum configuration required to work

DJANGO_NAMEKO_STANDALONE_APPS = ("<my_django_app>",)
INSTALLED_APPS = ("<mi_django_app>",)
SECRET_KEY = '<your_secret_key>'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<database>',
        'USER': '<user>',
        'HOST': '<host>',
        'PORT': 5432,
    }
}
```

## Testing
### Run tests with setup.py
You need to have installed setuptools
```bash
pip install setuptools
```

To test the package run in a shell, it will run the tests using pytest with the interpreter used against the Django version available to install (>=1.11,<=2.2.2).
```bash
python3 setup.py test
```

### Run tests with tox
You need to have install tox
```bash
pip install tox
```

Once satisfied, simply run the tox command
```bash
tox
```
It will run a bunch of tests using python3.6 and multiple django versions

## Example
### Example scafolding
* my_nameko_service
    * services.py
    * settings.py
    * requirements.txt
    * app1
        * \_\_init\_\_.py
        * models.py
    * app2
        * \_\_init\_\_.py
        * models.py
    
### Example usage
```python
from django_nameko_standalone import DjangoModels
from nameko.rpc import rpc


class NamekoService:
    name = "nameko_service"
    models = DjangoModels()  # Inject the django model dependency

    @rpc
    def get_items(self, host):
        items = self.models.Item.objects.all()
        ...

```
