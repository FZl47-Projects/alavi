from core.utils import get_timesince_persian
from account.models import User
from django.db import models
from .enums import Days
import datetime


# Foods model
class Food(models.Model):
    title = models.CharField('Title', max_length=128, default='')
    calories = models.PositiveIntegerField('Calories', default=0)

    class Meta:
        ordering = '-id',


# Sports model
class Sport(models.Model):
    title = models.CharField('Title', max_length=128, default='')

    class Meta:
        ordering = '-id',


# Diet program categories
class DietProgramCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diet_program_category')
    title = models.CharField('Title', max_length=256)

    created_at = models.DateTimeField('Create time', auto_now_add=True)
    modified_at = models.DateTimeField('Modify time', auto_now=True)

    class Meta:
        ordering = ('id',)

    def get_created_at_time_past(self):
        return get_timesince_persian(self.created_at)

    def __str__(self):
        return f'{self.user} - {self.title}'


# Training program categories
class TrainingProgramCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='training_program_category')
    title = models.CharField('Title', max_length=256)

    created_at = models.DateTimeField('Create time', auto_now_add=True)
    modified_at = models.DateTimeField('Modify time', auto_now=True)

    class Meta:
        ordering = ('id',)

    def get_created_at_time_past(self):
        return get_timesince_persian(self.created_at)

    def __str__(self):
        return f'{self.user} - {self.title}'


class DietProgramFree(models.Model):
    DayChoices = Days

    day = models.CharField(max_length=15, choices=DayChoices.choices, default=DayChoices.SATURDAY)
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, related_name='food_diet_programs_free', null=True)
    amount = models.PositiveIntegerField("amount", default=0)
    energy = models.PositiveIntegerField("Energy", default=0)
    description = models.TextField("Information", null=True)

    created_at = models.DateTimeField("Create time", auto_now_add=True)
    modified_at = models.DateTimeField("Modify time", auto_now=True)

    class Meta:
        ordering = '-id',

    @property
    def is_new(self):
        t_weak = datetime.datetime.now() - datetime.timedelta(days=1)
        if self.created_at > t_weak:
            return True
        return False

    def get_created_at(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

    def get_created_at_time_past(self):
        return get_timesince_persian(self.created_at)


class DietProgram(models.Model):
    DayChoices = Days

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_diet_program', default='')
    category = models.ForeignKey(DietProgramCategory, on_delete=models.CASCADE, related_name='diet_program_object')
    day = models.CharField(max_length=15, choices=DayChoices.choices, default=DayChoices.SATURDAY)
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, related_name='food_diet_programs', null=True)
    amount = models.PositiveIntegerField('amount', default=0)
    energy = models.PositiveIntegerField('Energy', default=0)
    description = models.TextField('Information', null=True)

    created_at = models.DateTimeField('Create time', auto_now_add=True)
    modified_at = models.DateTimeField('Modify time', auto_now=True)

    class Meta:
        ordering = '-id',

    @property
    def is_new(self):
        t_weak = datetime.datetime.now() - datetime.timedelta(days=1)
        if self.created_at > t_weak:
            return True
        return False

    def get_created_at(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

    def get_created_at_time_past(self):
        return get_timesince_persian(self.created_at)


class TrainingProgram(models.Model):
    DayChoices = Days

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_training_program', default='')
    category = models.ForeignKey(TrainingProgramCategory, on_delete=models.CASCADE, related_name='training_program_object')
    day = models.CharField(max_length=15, choices=DayChoices.choices, default=DayChoices.SATURDAY)
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, related_name='sport_training_programs', null=True)
    rep = models.PositiveIntegerField('Repeat', default=0)
    sets = models.PositiveIntegerField('Set', default=0)
    description = models.TextField('Description', null=True)

    created_at = models.DateTimeField('Create time', auto_now_add=True)
    modified_at = models.DateTimeField('Modify time', auto_now=True)

    class Meta:
        ordering = '-id',

    @property
    def is_new(self):
        t_weak = datetime.datetime.now() - datetime.timedelta(days=1)
        if self.created_at > t_weak:
            return True
        return False

    def get_created_at(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

    def get_created_at_time_past(self):
        return get_timesince_persian(self.created_at)


# Diet meals
class DietMeal(models.Model):
    title = models.CharField('Title', max_length=128)
    time = models.TimeField('Meal Time', max_length=64, null=True, blank=True)

    created_at = models.DateTimeField('Create time', auto_now_add=True)
    modified_at = models.DateTimeField('Modify time', auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.title} - {self.title}'
