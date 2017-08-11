# cs3773-group9
Two apps that were used in this project were django-allauth and django-scheduler

# Django-scheduler
Installation
========

```bash
pip install django-scheduler
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

If necessary, install bower dependencies with:

```
./manage.py bower install
```

Remember to execute "python manage.py collectstatic"

# Django-allauth

Installation
============

Django
------

Python package::

    pip install django-allauth

Post-Installation (if necessary)
-----------------

In your Django root execute the command below to create your database tables::

    ./manage.py migrate
