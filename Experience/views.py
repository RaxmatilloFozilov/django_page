from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Experience</h1>")

def Sarlavha(requests):
    return render(requests,"index.html")

# Create your views here.
