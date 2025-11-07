from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import DishType, Dish, Ingredient, Cook


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
        }


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
            "description": forms.TextInput(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
            "price": forms.TextInput(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
            "dish_type": forms.Select(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
            "ingredients": forms.CheckboxSelectMultiple(attrs={
                "class": "form-control border border-dark border-2 shadow-lg"},),
            "cooks": forms.SelectMultiple(attrs={
                "class": "form-control border border-dark border-2 shadow-lg"}, ),
        }

    def clean_price(self):
        return validate_price(self.cleaned_data["price"])

def validate_price(price):
    if price <= 0:
        raise ValidationError("Price must be greater than 0")


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
        }


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
            "years_of_experience": forms.NumberInput(attrs={
                "type": "number",
                "min": 0,
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
            "first_name": forms.TextInput(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
            "last_name": forms.TextInput(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
            "password": forms.PasswordInput(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
            "password2": forms.PasswordInput(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
        }

    def clean_years_of_experience(self):
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["years_of_experience", "first_name", "last_name"]

        widgets = {
            "years_of_experience": forms.NumberInput(attrs={
                "type": "number",
                "min": 0,
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
            "first_name": forms.TextInput(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
            "last_name": forms.TextInput(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
        }

    def clean_years_of_experience(self):
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


def validate_years_of_experience(years_of_experience):
    if years_of_experience < 0:
        raise ValidationError("Years of experience must be greater or equal 0")


    return years_of_experience

class CookNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by name",
            "class": "form-control form-control-lg border border-light border-2 shadow-lg",
            "style": "color:white;"
        })
    )


class IngredientNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by ingredient name",
            "class": "form-control form-control-lg border border-light border-2 shadow-lg",
            "style": "color:white;"
        })
    )


class DishNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by dish name",
            "class": "form-control form-control-lg border border-light border-2 shadow-lg",
            "style": "color:white;"
        })
    )