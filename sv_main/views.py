from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import Http404
from .models import *
from .constants import DEFAULT_VESSEL_IMAGE, DEFAULT_CATEGORY_IMAGE


# Create your views here.
def mainpage(request):
    vesslist = Vessel.objects.all
    return render(request, 'main_page.html', {
        'DEFAULT_VESSEL_IMAGE': DEFAULT_VESSEL_IMAGE,
        'DEFAULT_CATEGORY_IMAGE': DEFAULT_CATEGORY_IMAGE,
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
    pass


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
