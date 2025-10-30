from django.contrib import admin

from kitchen_app.models import Dish, Ingredient, DishType, Cook

admin.site.register(Cook)
admin.site.register(DishType)
admin.site.register(Ingredient)
admin.site.register(Dish)
