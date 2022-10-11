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


