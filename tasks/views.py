from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("<h1 style='color:blue'>Hello, this is the home page.</h1>")
def show_task(request):
    return HttpResponse("<h1 style='color:red'>Hello, this is the show_task page.</h1>")
