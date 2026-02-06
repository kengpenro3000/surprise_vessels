from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import Http404
from .models import *
from .constants import *

import random 
import json
import ast

def mainpage(request):
    vessel = random.choice(Vessel.objects.all())
    vessel_id = vessel.id
    # 'vessel' : vessel
    print(vessel_id)
    return render(request, 'main_page.html', {
        'DEFAULT_VESSEL_IMAGE': DEFAULT_VESSEL_IMAGE,
        'DEFAULT_CATEGORY_IMAGE': DEFAULT_CATEGORY_IMAGE,
        'vessel' : vessel

    })




def start_poll(request):

    vessel = random.choice(Vessel.objects.all())
    vessel_id = vessel.id
    
    if  request.method == "POST":
        if request.POST.get("start_poll_button") == "start":
            print("yes it works")    
            questions = []
            for x in Question.objects.all():
                questions.append(x.id)
                print(questions)
            random.shuffle(questions)
            request.session["queue"] = questions
            request.session["temp_results"] = DEFAULT_PARAMETERS

            return redirect('poll_page') 
    return  render(request, "poll_start.html", {'vessel' : vessel})


def poll(request):

    vessel = random.choice(Vessel.objects.all())
    vessel_id = vessel.id
    


    # if request.method == "POST":
    #     for key, value in request.POST.items():
            # if key == 'csrfmiddlewaretoken':
            #     continue
            # print(value)
            # dict_value = ast.literal_eval(value)
            # for key in dict_value.keys():
            #     request.session["temp_results"][key] += dict_value[key]
        
    # return  render(request, "poll_page.html", {
    #     "question" : Question.objects.get(pk = question_id),
    #     "answer" : answers,
    #     "questions" : questions
    # })

    if request.method == "POST":

        if request.POST.get("poll_button") == "go":
           
                return redirect('/poll/')
        elif request.POST.get("poll_button") == "end":
          return redirect('poll_results')  
        
        for key, value in request.POST.items():
                if key == 'csrfmiddlewaretoken':
                    continue
                print(value)
                dict_value = ast.literal_eval(value)
                for key in dict_value.keys():
                    request.session["temp_results"][key] += dict_value[key]
    else:
        if len(request.session["queue"]) == 0:
            return redirect('poll_results_page')
        question_id = request.session["queue"][0]
        questions = len(Question.objects.all())
        print(question_id, "|", questions)
        answers = list(Answer.objects.filter(question = Question.objects.get(pk = question_id)))
        random.shuffle(answers)

        temp_queue = request.session["queue"]
        print(temp_queue.pop(0))
        request.session["queue"] = temp_queue

        print(request.session["queue"])


    return  render(request, "poll_page.html", {
        "question" : Question.objects.get(pk = question_id),
        "answer" : answers,
        "questions" : questions,
        'vessel' : vessel
    })


def poll_results(request):
    vessel = random.choice(Vessel.objects.all())
    vessel_id = vessel.id
    

    results = Results.objects.create()

    answer_parameters = DEFAULT_PARAMETERS #(это session.temp_results)


    results.calculate_nearest_cat(answer_parameters)

    context = {
        "a": answer_parameters["a"],
        "b": answer_parameters["b"],
        "c": answer_parameters["c"],
        "final_cat": results.final_cat,
        'vessel' : vessel
    }

    return render(request, "poll_results.html", context) 


def vessels(request):
    vesslist = Vessel.objects.all().order_by("name")
    return render(request, "vessels_page.html", {
        "vesslist": vesslist,
        "DEFAULT_VESSEL_IMAGE": DEFAULT_VESSEL_IMAGE,

    'vessel' : vessel
    })


def single_vessel(request, vessel_id):
    vessel = random.choice(Vessel.objects.all())
    vessel_id = vessel.id
    category = vessel.category
    category_id = category.id

    return render(request, "vessel.html", {
        "vessel": vessel,
        "DEFAULT_VESSEL_IMAGE": DEFAULT_VESSEL_IMAGE,
        'category_id': category_id
    })


def categories(request, ):
    vessel = random.choice(Vessel.objects.all())
    vessel_id = vessel.id

    catlist = VesselCategory.objects.all().order_by("name")
    template = loader.get_template("categories_page.html")
    return HttpResponse(render(request, "categories_page.html", {
        "catlist": catlist,
        "DEFAULT_CATEGORY_IMAGE": DEFAULT_CATEGORY_IMAGE,

    'vessel' : vessel
    

    }))


def single_category(request, category_id):
    vessel = random.choice(Vessel.objects.all())
    vessel_id = vessel.id



    try:
        category = VesselCategory.objects.get(pk=category_id)
    except:
        raise Http404("нет категории")
    vess_for = Vessel.objects.filter(category=category)
    return HttpResponse(render(request, "category.html", {
        "category": category,
        "vess_for": vess_for,
        "DEFAULT_VESSEL_IMAGE": DEFAULT_VESSEL_IMAGE,
        "DEFAULT_CATEGORY_IMAGE": DEFAULT_CATEGORY_IMAGE,

    'vessel' : vessel

    }))

def stat_page(request):
    vessel = random.choice(Vessel.objects.all())
    vessel_id = vessel.id


    sorted_cats = []
    all_results = Results.objects.all().count()

    for cat in VesselCategory.objects.all():
   
        persentage = cat.calculate_cat_rating()  //  all_results * 100
     
        sorted_cats.append([cat, cat.calculate_cat_rating(), persentage])
    

        sorted_cats.sort(reverse=True, key = lambda x : x[1])
    
    return render(request, "stat_page.html", {
        "sorted_cats" : sorted_cats,

    'vessel' : vessel

    })

