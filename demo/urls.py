from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Another, BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', BookViewSet)
## to use as <mainurl>/demo
urlpatterns = [
    path('first', views.first),
    path('', include(router.urls)),
    path('first1', views.first1),
    path('firstfunction', views.firstfunction),
    path('another', Another.as_view()),
]

