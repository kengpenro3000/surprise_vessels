from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *


# Create your views here.
def mainpage (request):
    vesslist = Vessel.objects.all
    return render(request, 'main_page.html')

def poll(request):
    return render(request, "poll_page.html")

def vessels(request):
    vesslist = Vessel.objects.all().order_by("name")
    return render(request, "vessels_page.html", {"vesslist" : vesslist})

def categories(request):
    catlist = VesselCategory.objects.all().order_by("name")
    template = loader.get_template("categories_page.html")
    return HttpResponse(render(request, "categories_page.html", {"catlist" : catlist}))