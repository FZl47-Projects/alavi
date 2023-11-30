from django import forms
from . import models


# Add food form
class FoodAdd(forms.ModelForm):
    class Meta:
        model = models.Food
        fields = '__all__'
