from django import forms
from . import models


class FoodAdd(forms.ModelForm):
    class Meta:
        model = models.Food
        fields = '__all__'


class SportAdd(forms.ModelForm):
    class Meta:
        model = models.Sport
        fields = '__all__'
