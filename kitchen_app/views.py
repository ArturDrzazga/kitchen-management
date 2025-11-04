from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Cook, DishType, Dish



def index(request):
    num_cooks = get_user_model().objects.all().count()
    num_dish_types = DishType.objects.all().count()
    num_dishes = Dish.objects.all().count()

    context = {
        'num_cooks': num_cooks,
        'num_dish_types': num_dish_types,
        'num_dishes': num_dishes,
    }

    return render(request, "kitchen/index.html", context=context)