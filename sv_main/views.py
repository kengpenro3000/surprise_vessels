from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def mainpage (request):
    return render(request, 'main_page.html')

def poll(request):
    return render(request, "poll_page.html")

def vessels(request):
    return render(request, "vessels_page.html")

def categories(request):
    return render(request, "categories_page.html")