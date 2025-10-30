from django.urls import path

from kitchen_app.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "kitchen_app"