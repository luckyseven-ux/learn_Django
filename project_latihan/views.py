
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def index2(request):
    return HttpResponse("<h1>Welcome to Our Home Page<h1>")

def about2(request):
    return HttpResponse("<h1>This is about page<h1>")