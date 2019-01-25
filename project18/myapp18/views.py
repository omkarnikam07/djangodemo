from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
        return HttpResponse("Welcome to MyApp18 application")

def AddStudent(request):
        return HttpResponse("Welcome to MyApp81 application")
