import datetime
from django.db import models
from account.models import User
from core.utils import get_timesince_persian

Day_choices = (
    ('0', 'شنبه'), ('1', 'یکشنبه'), ('2', 'دوشنبه'),
    ('3', 'سه شنبه'), ('4', 'چهارشنبه'), ('5', 'پنجشنبه'),
    ('6', 'جمعه')
)


class Food(models.Model):
    name = models.CharField("Name", max_length=100)

    class Meta:
        ordering = '-id',


class Sport(models.Model):
    name = models.CharField("Name", max_length=100)

    class Meta:
        ordering = '-id',


class Diet_program_object_free(models.Model):
    day = models.CharField(max_length=15, choices=Day_choices)
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, related_name='food_diet_programs_free', null=True)
    amount = models.PositiveIntegerField("amount", default=0)
    energy = models.PositiveIntegerField("Energy", default=0)
    description = models.TextField("Information", null=True)
    created_time = models.DateTimeField("Created_time", auto_now_add=True)
    moified_time = models.DateTimeField("Modified_time", auto_now=True)

    class Meta:
        ordering = '-id',

    @property
    def is_new(self):
        t_weak = datetime.datetime.now() - datetime.timedelta(days=1)
        if self.created_time > t_weak:
            return True
        return False

    def get_created_at(self):
        return self.created_time.strftime('%Y-%m-%d %H:%M:%S')

    def get_created_at_timepast(self):
        return get_timesince_persian(self.created_time)


class Diet_program_object(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_diet_program', default='')
    day = models.CharField(max_length=15, choices=Day_choices)
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, related_name='food_diet_programs', null=True)
    amount = models.PositiveIntegerField("amount", default=0)
    energy = models.PositiveIntegerField("Energy", default=0)
    description = models.TextField("Information", null=True)
    created_time = models.DateTimeField("Created_time", auto_now_add=True)
    moified_time = models.DateTimeField("Modified_time", auto_now=True)

    class Meta:
        ordering = '-id',

    @property
    def is_new(self):
        t_weak = datetime.datetime.now() - datetime.timedelta(days=1)
        if self.created_time > t_weak:
            return True
        return False

    def get_created_at(self):
        return self.created_time.strftime('%Y-%m-%d %H:%M:%S')

    def get_created_at_timepast(self):
        return get_timesince_persian(self.created_time)


class Training_program_object(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_training_program', default='')
    day = models.CharField(max_length=15, choices=Day_choices)
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, related_name='sport_training_programs', null=True)
    rep = models.PositiveIntegerField("Repeat", default=0)
    sets = models.PositiveIntegerField("Set", default=0)
    description = models.TextField("Information", null=True)
    created_time = models.DateTimeField("Created_time", auto_now_add=True)
    moified_time = models.DateTimeField("Modified_time", auto_now=True)

    class Meta:
        ordering = '-id',

    @property
    def is_new(self):
        t_weak = datetime.datetime.now() - datetime.timedelta(days=1)
        if self.created_time > t_weak:
            return True
        return False

    def get_created_at(self):
        return self.created_time.strftime('%Y-%m-%d %H:%M:%S')

    def get_created_at_timepast(self):
        return get_timesince_persian(self.created_time)
