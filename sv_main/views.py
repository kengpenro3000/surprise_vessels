from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import Http404
from .models import *
from .constants import *



def mainpage(request):

    return render(request, 'main_page.html', {
        'DEFAULT_VESSEL_IMAGE': DEFAULT_VESSEL_IMAGE,
        'DEFAULT_CATEGORY_IMAGE': DEFAULT_CATEGORY_IMAGE,

    })




def start_poll(request):

    #if request.session.queue:
        #отрисовать обе кнопки

    #кнопка начать тест

        #создается очередь в сешшнс request.session.queue = list(Question.objects.all()) (можно перемешать)
        #создается словарь со временными результатами
        #переход на poll

    #кнопка продолжить тест
        #переход на poll



    #return render(request, "poll_start.html")


def poll(request):

    #ловим из сешшнс очередь
    #если остался последний вопрос, рисуем кнопку закончить тест вместо продолжить

    #берем первый вопрос, рисуем форму со всеми его ответами (можно перемешать)
    #убираем из очереди

    #ловим значение ответа из формы, прибавляем его попунктно в temp_result
    # 
    # вызываем опять poll по кнопке продолжить (на тот же урл перейти)
    # по кнопке закончить тест в poll_results  


    # questions = Question.objects.all()

    # context = {
    #     "questions": questions,
    # }
    # return render(request, "poll_page.html", context)


def poll_results(request):
    results = Results.objects.create()

    # cont = 0
    # answer_parameters = DEFAULT_PARAMETERS (это session.temp_results)

    #это унести в poll
    #if request.method == "POST":
        # for key, value in request.POST.items():
        #     if cont == 0:
        #         cont += 1 
        #         continue
        #     print(value)
        #     for key in value.keys():
        #         answer_parameters[key] += value.key

            # answer_parameters["a"] += value.a
            # answer_parameters["b"] += value.b
            # answer_parameters["c"] += value.c

    results.calculate_nearest_cat(answer_parameters)

    context = {
        "a": answer_parameters["a"],
        "b": answer_parameters["b"],
        "c": answer_parameters["c"],
        "final_cat": results.final_cat
    }

    return render(request, "poll_results.html", context) 


def vessels(request):
    vesslist = Vessel.objects.all().order_by("name")
    return render(request, "vessels_page.html", {
        "vesslist": vesslist,
        "DEFAULT_VESSEL_IMAGE": DEFAULT_VESSEL_IMAGE,
    })


def single_vessel(request, vessel_id):
    try:
        vessel = Vessel.objects.get(pk=vessel_id)
    except:
        raise Http404("Нет сосуда")
    return render(request, "vessel.html", {
        "vessel": vessel,
        "DEFAULT_VESSEL_IMAGE": DEFAULT_VESSEL_IMAGE,
    })


def categories(request, ):
    catlist = VesselCategory.objects.all().order_by("name")
    template = loader.get_template("categories_page.html")
    return HttpResponse(render(request, "categories_page.html", {
        "catlist": catlist,
        "DEFAULT_CATEGORY_IMAGE": DEFAULT_CATEGORY_IMAGE,
    }))


def single_category(request, category_id):
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
    }))

def stat_page(request):
    sorted_cats = []
    all_results = Results.objects.all().count()

    for cat in VesselCategory.objects.all():
   
        persentage = cat.calculate_cat_rating()  //  all_results * 100
     
        sorted_cats.append([cat, cat.calculate_cat_rating(), persentage])
    

        sorted_cats.sort(reverse=True, key = lambda x : x[1])
    
    return render(request, "stat_page.html", {
        "sorted_cats" : sorted_cats
    })

