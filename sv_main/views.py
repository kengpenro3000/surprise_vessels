from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def mainpage (request):
    #template = loader.get_template('templates/mainpage.html')
<<<<<<< HEAD
    return HttpResponse('hello world from mainpage view!')
=======
    #return HttpResponse('hello world from mainpage view!')
    return render(request, 'main_page.html')

def poll(request):
    return render(request, "poll_page.html")

def vessels(request):
    return render(request, "vessels_page.html")

def categories(request):
    return render(request, "categories_page.html")
>>>>>>> a6a4391 (create new pages, make in them header and footer and connect urls)
