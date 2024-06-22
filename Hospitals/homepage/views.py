

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

 # Create your views here.

def index(request):
     return HttpResponse("Hello, ")

def index(request):
    template = "homepage/index.html"
    return render(request, "templates")

