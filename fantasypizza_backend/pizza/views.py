from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")

def get_ingridients(request):
    return HttpResponse()

def get_ingridient(request, ingredient_id):
    return HttpResponse()
