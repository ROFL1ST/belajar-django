from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def index2(request):
    return HttpResponse("<h1>Ini adalah Home</h1>")

def about(request):
    return HttpResponse("<h1>Ini adalah about</h1>")


