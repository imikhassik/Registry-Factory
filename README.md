# Registry

## Create registry
To create a registry run: 
```commandline
python manage.py createregistry --template=registry_template.zip <your_registry> --model_name=<Your_model>
```
Example:
```commandline
python manage.py createregistry --template=registry_template.zip people --model_name=Person
```

In  registry_factory/settings.py:
- add <your_registry> to the list of INSTALLED_APPS before 'drf_spectacular'

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registry_config',
    'links',
    'rest_framework',
    'django_filters',
    'people',  # <-- the newly installed registry
    'drf_spectacular',
]
```

Create and apply db migrations:
```commandline
python manage.py makemigrations
python manage.py migrate
```

## Register API endpoints
In  registry_factory/urls.py:
- from <your_registry>.views import <Your_objects>Viewset, <Your_object>Viewset
- register the new endpoints with the router

```python
from links.views import LinksViewset, LinkViewset
from people.views import PeopleViewset, PersonViewset  # <-- newly imported viewsets


router = routers.DefaultRouter()
router.register(r'links', LinksViewset)
router.register(r'link', LinkViewset)
router.register(r'people', PeopleViewset)  # <-- nnew endpoind
router.register(r'person', PersonViewset)  # <-- nnew endpoind
```

## Test
Run
```commandline
python manage.py test people
```
or for a detailed test report
```commandline
coverage run manage.py test people
```
See https://coverage.readthedocs.io/en/7.2.7/cmd.html#reporting for generating a test report
___

Start server
```commandline
python manage.py runserver
```
Swagger UI: http://127.0.0.1:8000/swagger-ui/
