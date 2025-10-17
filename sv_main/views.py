from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def mainpage(request):
    #template = loader.get_template('templates/mainpage.html')
    #return HttpResponse('hello world from mainpage view!')
    return render(request, 'mainpage.html')