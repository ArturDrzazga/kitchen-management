from django.urls import path

from kitchen_app.views import index, TypesOfDishesListView, TypesOfDishesCreateView

urlpatterns = [
    path("", index, name="index"),
    path("types-of-dishes/",
         TypesOfDishesListView.as_view(),
         name="dishtype-list"),
    path("types-of-dishes/create/",
         TypesOfDishesCreateView.as_view(),
         name="dishtype-create"),
]

app_name = "kitchen_app"