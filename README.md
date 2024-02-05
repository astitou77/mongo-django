Install Python : https://www.python.org

Install Python module django:
> py -3.10 -m pip list installed
> py -3.10 -m django --version
> py -3.10 -m pip install django==4.0.2
> py -3.10 -c "import django; print(django.__path__)"

Start Django Project 
> django-admin.py startproject myProjectName
> cd myProjectName
> py -3.10 manage.py runserver 0.0.0.0:8000


Start First Django App
> py -3.10 -m manage startapp myNewApp
> Settings : INSTALLED_APPS = [ 'myNewApp.apps.MynewappConfig', ]
