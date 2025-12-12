from django.urls import path

from . import views

urlpatterns = [
    path("", views.mainpage, name="main_page"),
    path("start-poll/", views.start_poll, name="poll_start"),
    path("poll/", views.poll, name="poll_page"), 
    path("vessels/", views.vessels, name="vessels_page"), 
    path("categories/", views.categories, name="categories_page"),
    path("vessels/<int:vessel_id>/", views.single_vessel, name="single_vessel_page"),
    path("categories/<int:category_id>", views.single_category, name="single_category_page"),
    path("categories/<int:category_id>", views.single_category, name="single_category_page")
]