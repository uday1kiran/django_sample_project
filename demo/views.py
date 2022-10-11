from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Book

# Create your views here.
def first(request):
    return HttpResponse('First message from Views')

def firstfunction(request):
    return HttpResponse('First message from Views')

class Another(View):
    books = Book.objects.all()  ## to display all objects of that model.
    ## books = Book.objects.filter(is_published=True)
    ## books = Book.objects.get(is_published=True) ## filter will get all objects with that field value, but get will being only one object
    ## book = Book.objects.get(id=2)
    #output = f"We have {len(books)} books in DB"
    output = ''
    for book in books:
        output += f"We have {book.title} book in DB with ID: {book.id}<br>"

    def get(self, request):
        return HttpResponse(self.output)