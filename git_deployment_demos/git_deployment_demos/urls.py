import time

from django.contrib import admin
from django.shortcuts import render
from django.urls import path


def index(request):
    return render(request, "index.html")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index)
]

'''
/Users/doncho/repos/softuni/python-web-frameworks-demos/git_deployment_demos/.venv/bin/python

/Users/doncho/repos/softuni/python-web-frameworks-demos/git_deployment_demos/manage.py
x
runserver localhost:8000


=> python manage.py runserver localhost:8000 # Only for development purposes

`python manage.py runserver`:
1. Automatic reloading of the WSGI application when code changes
2. Serves static files from the `STATIC_DIRS` setting
3. Single-threaded

`gunicorn`:
1. Stable running of the application
2. Does not serve static files (NGINX)
3. Multi-threaded

'''
