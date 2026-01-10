from django.urls import path

from . import views

urlpatterns = [
    path("", views.mainpage, name="main_page"),
    path("start-poll/", views.start_poll, name="poll_start"),
    path("poll/", views.poll, name="poll_page"), 
    path("poll-results/", views.poll_results, name="poll_results_page"),
    path("items/", views.items, name="items_page"), 
    path("categories/", views.categories, name="categories_page"),
    path("items/<int:item_id>/", views.single_item, name="single_item_page"),
    path("categories/<int:category_id>", views.single_category, name="single_category_page"),
    # path("form_test/", views.form_test, name="form_test_page"),
    # path("form_test_res/", views.form_test_res, name="form_test_res_page"),

]