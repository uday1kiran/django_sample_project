from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
def first(request):
    return HttpResponse('First message from Views')

def firstfunction(request):
    return HttpResponse('First message from Views')

class Another(View):
    def get(self, request):
        return HttpResponse('This is another function inside class')