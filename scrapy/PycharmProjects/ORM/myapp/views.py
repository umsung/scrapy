from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from myapp.models import *

def test(request, tag):
    person = Person.objects.get(first_name=tag)
    person.delete()

    return HttpResponse('{}被删除了'.format(tag))