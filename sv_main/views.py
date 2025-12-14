from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import Http404
from .models import *
from .constants import DEFAULT_VESSEL_IMAGE, DEFAULT_CATEGORY_IMAGE



def mainpage(request):
    pop_catslist = VesselCategory.objects.order_by("-rating")[:3]
    return render(request, 'main_page.html', {
        'DEFAULT_VESSEL_IMAGE': DEFAULT_VESSEL_IMAGE,
        'DEFAULT_CATEGORY_IMAGE': DEFAULT_CATEGORY_IMAGE,
        "pop_catslist": pop_catslist
    })



def start_poll(request):
    return render(request, "poll_start.html")


def poll(request):

    # сделать форму с вопросами и ответами

    questions = Question.objects.all()
    # ответы для каждого вопроса
    answers = {}
    # for q in questions:
    #     answers[q.id] = Answer.objects.filter(question=q)
    # передать в шаблон вопросы и ответы
    context = {
        "questions": questions,
        # "answers": answers,
    }

    # рендерится пользовательская форма с вопросами и ответами
    return render(request, "poll_page.html", context)

    # кнопка отправить ловит ответы
    # создается result
    # results = Results.objects.create()
    # вызывается в result обсчет итогов
    # results.calculate_nearest_cat()
    # result.save()
    #

    # results = Results.objects.get(pk = 23)
    # редиректом перейти на страницу с результатами

    return render(request, "poll_page.html", {"res": results})

def poll_results(request):
    results = Results.objects.create()
    cont = 0
    answer_parameters = {"a": 0,"b": 0,"c": 0}

    if request.method == "POST":
        for key, value in request.POST.items():
            if cont == 0:
                cont += 1 
                continue
            print(value)
            answer_parameters["a"] += int(value.split()[0])
            answer_parameters["b"] += int(value.split()[1])
            answer_parameters["c"] += int(value.split()[2])

    results.calculate_nearest_cat(answer_parameters)

    context = {
        "a": answer_parameters["a"],
        "b": answer_parameters["b"],
        "c": answer_parameters["c"],
        "final_cat": results.final_cat
    }

    return render(request, "poll_results.html", context) 


def form_test_res(request):
    context = {}
    if request.method == "POST":
         for key, value in request.POST.items():
            request.session["post_key"] = key
            request.session["post_value"] = value
    return redirect("form_test_page")


def form_test(request):
    keys = request.session.get("post_key", None)
    values = request.session.get("post_value", None)
    return render(request, "form_test.html", {"keys": keys, "values": values})


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


# def vessel_for_category(request, category_id):
#     vess_for = Vessel.objects.get(category = category_id)
#     return render(request, "category.html", {"vess_for"})
