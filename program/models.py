from django.db import models
from account.models import User


Day_choices= (
    ('0', 'Sat'), ('1', 'Sun'), ('2', 'Mon'),
    ('3', 'Tue'), ('4', 'Wed'), ('5', 'Thu'), 
    ('6', 'fri')
)



class Day(models.Model):
    day = models.CharField("Day",choices=Day_choices, max_length=10)
    
class Food(models.Model):
    name = models.CharField("Name", max_length=100)
    
class Sport(models.Model):
    name = models.CharField("Name", max_length=100)
    

class Diet_program_object(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_diet_program',default='')
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='diet_program_objects')
    food = models.ForeignKey(Food,on_delete=models.SET_NULL,related_name='food_diet_programs',null=True)
    quantity = models.PositiveIntegerField("quantity",default=0)
    energy = models.PositiveIntegerField("Energy",default= 0)
    info = models.TextField("Information")
    created_time = models.DateField("Created_time", auto_now_add=True)
    moified_time = models.DateField("Modified_time", auto_now=True)

class Training_program_object(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_training_program',default='')
    day = models.ForeignKey(Day, on_delete=models.CASCADE, max_length=100, related_name='training_program_objects')
    sport = models.ForeignKey(Sport,on_delete=models.SET_NULL,related_name='sport_training_programs',null=True)
    rep = models.PositiveIntegerField("Repeat",default=0)
    sets = models.PositiveIntegerField("Set",default= 0)
    info = models.TextField("Information")
    created_time = models.DateField("Created_time", auto_now_add=True)
    moified_time = models.DateField("Modified_time", auto_now=True)
