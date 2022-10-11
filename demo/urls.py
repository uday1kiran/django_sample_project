from django.contrib import admin
from django.urls import path
from . import views
from .views import Another

## to use as <mainurl>/demo
urlpatterns = [
    path('', views.first),
    path('firstfunction', views.firstfunction),
    path('another', Another.as_view()),
]