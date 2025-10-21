from django.urls import path

from . import views

urlpatterns = [
    path("", views.mainpage, name="main_page"),
    path("poll/", views.poll, name="poll_page"), 
    path("vessels/", views.vessels, name="vessels_page"), 
    path("categories/", views.categories, name="categories_page")
]