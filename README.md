
# DjangoRunCommands


A Python Django library which helps you to run management commands from admin dashboard.


Quick start
-----------

1. Add "django_run_command" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_run_command',
    ]

2. Add commands to be run from admin in your settings file like::
    
    ``COMMAND_CHOICES = (
      ('collectstatic', "Collectstatic"),
      ('loaddata', "Loaddata"),
  )``

3. Run ``python manage.py migrate`` to create the django_run_command models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to run your management commands from admin (you'll need the Admin app enabled).

5. This repository is open source feel free to contribute.

