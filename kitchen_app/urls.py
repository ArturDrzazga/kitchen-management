from django.urls import path

from kitchen_app import views

urlpatterns = [
    path("", index, name="index"),
]
