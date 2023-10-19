from django import forms
from . import models


# Add food form
class FoodAdd(forms.ModelForm):
    class Meta:
        model = models.Food
        fields = '__all__'


# Add sport form
class SportAdd(forms.ModelForm):
    class Meta:
        model = models.Sport
        fields = '__all__'


# Add DietProgramCategory form
class DietProgramCategoryForm(forms.ModelForm):
    class Meta:
        model = models.DietProgramCategory
        fields = '__all__'

    