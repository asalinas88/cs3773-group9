# cs3773-group9
Installation
========

```bash
pip install django-scheduler
```

edit your `settings.py`

add to `INSTALLED_APPS`:

```python
'schedule',
```

add to `TEMPLATE_CONTEXT_PROCESSORS`:

```python
"django.template.context_processors.request"
```

Static assets
=============

Django Scheduler relies on [jQuery](https://jquery.com/) and
[Bootstrap](https://getbootstrap.com/) to provide its user
interface. If you don't need help with adding these to your Django
project, you can skip the next step where we will show you how to add
them to your Django project.

```bash
npm install -g bower
pip install django-bower
```

edit your `settings.py`

add to `INSTALLED_APPS`:

```python
'djangobower',
```

Add staticfinder to `STATICFILES_FINDERS`:

```
'djangobower.finders.BowerFinder',
```

Specify the path to the components root (you need to use an absolute
path):

```
BOWER_COMPONENTS_ROOT = '/PROJECT_ROOT/components/'
```

Add the following Bower dependencies for scheduler:

```
BOWER_INSTALLED_APPS = (
    'jquery',
    'jquery-ui',
    'bootstrap'
)
```

Last step, install bower dependencies with:

```
./manage.py bower install
```

Remember to execute "python manage.py collectstatic"
