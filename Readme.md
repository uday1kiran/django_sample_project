mkdir tutorial
cd tutorial
python3 -m venv venv

for mac:
-----------
source venv/bin/activate
pip install Django


for windows:
------------
venv\Scripts\activate
pip install Django


django-admin startproject first .
python3 manage.py runserver


www.jetbrains.com/pycharm/download
download community edition.

open project -- tutorial folder.
right click on manage.py -- edit configurations -- parameters (runserver)

django-admin startapp demo (or) python3 manage.py startapp demo

## data from installed apps need to be applied to database.
python manage.py migrate

models.py in demo app folder
-------
from django import models
class Book(models.Model):
 title = models.CharField(max_length=36)

Add entry for the demo app to the project settings.py INSTALLED_APPS section

python3 manage.py makemigrations
python3 manage.py migrate


login to admin page using below user created
---------
python manage.py createsuperuser
http://localhost:8000/admin

add an entry in admin.py for a model to display in admin page
----
admin.site.register(Book)


to add support to rest api:
---
pip install djangorestframework
add entry to settings.py INSTALLED_APPS rest_framework
and then run ... python3 manage.py migrate


to add auth token:
-
add 'rest_framework.authtoken', to installed_apps of settings.py of project
and project level urls.py  path('auth/',obtain_auth_token) 
this will add a token table in admin page.
http://127.0.0.1:8000/auth/ POST with username and pasword in form-data of body in postman.will create a token.
Authorization(Token token_value) --> in header of api request in postman.

pycharm shortcuts:
html5 skeleton - html:5<tab> 


