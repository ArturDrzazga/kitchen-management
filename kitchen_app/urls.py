from django.urls import path

from kitchen_app.views import (index,
                               TypesOfDishesListView,
                               TypesOfDishesCreateView,
                               TypesOfDishesUpdateView,
                               TypesOfDishesDeleteView,
                               DishesListView,
                               DishesCreateView, DishesUpdateView)

urlpatterns = [
    path("", index, name="index"),
    path("types-of-dishes/",
         TypesOfDishesListView.as_view(),
         name="dishtype-list"),
    path("types-of-dishes/create/",
         TypesOfDishesCreateView.as_view(),
         name="dishtype-create"),

    path("types-of-dishes/<int:pk>/update/",
         TypesOfDishesUpdateView.as_view(),
         name="dishtype-update"),

    path("types-of-dishes/<int:pk>/delete/",
         TypesOfDishesDeleteView.as_view(),
         name="dishtype-delete"),

    path("dishes/",
         DishesListView.as_view(),
         name="dish-list"),

    path("dishes/create/",
         DishesCreateView.as_view(),
         name="dish-create"),

    path("dishes/<int:pk>/update/",
         DishesUpdateView.as_view(),
         name="dish-update"),
]

app_name = "kitchen_app"