from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Book

def index(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', books), content_type='application/json')