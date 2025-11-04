from django.urls import path

from kitchen_app.views import index, TypesOfDishesListView

urlpatterns = [
    path("", index, name="index"),
    path("types-of-dishes/",
         TypesOfDishesListView.as_view(),
         name="dishtype-list"),
]

app_name = "kitchen_app"