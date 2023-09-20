from django.db import models
from account.models import User


Day_choices= (
    ('0', 'Sat'), ('1', 'Sun'), ('2', 'Mon'),
    ('3', 'Tue'), ('4', 'Wed'), ('5', 'Thu'), 
    ('6', 'fri')
)



class Days(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='days')
    day = models.CharField("Day",choices=Day_choices, max_length=10)
    

class Diet_program_object(models.Model):
    day = models.ForeignKey(Days, on_delete=models.CASCADE, related_name='diet_program_objects')
    food = models.CharField("food",blank=False,null=False,max_length=100)
    quantity = models.PositiveIntegerField("quantity",default=0)
    energy = models.PositiveIntegerField("Energy",default= 0)
    info = models.TextField("Information")

class Training_program_object(models.Model):
    day = models.ForeignKey(Days, on_delete=models.CASCADE, max_length=100, related_name='training_program_objects')
    name = models.CharField("Name",blank=False,null=False,max_length=100)
    rep = models.PositiveIntegerField("Repeat",default=0)
    sets = models.PositiveIntegerField("Set",default= 0)
    info = models.TextField("Information")
