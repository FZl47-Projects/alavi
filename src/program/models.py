from django.utils.translation import gettext as _
from core.utils import get_timesince_persian
from account.models import User
from .enums import DayChoices
from django.db import models
import datetime


# Foods model
class Food(models.Model):
    title = models.CharField('Food title', max_length=128)
    calories = models.PositiveIntegerField('Calories', default=0)

    class Meta:
        verbose_name = _('Food')
        verbose_name_plural = _('Foods')
        ordering = ('-id',)

    def __str__(self) -> str:
        return self.title


# Meals model
class Meal(models.Model):
    title = models.CharField('Meal title', max_length=128)
    time = models.TimeField('Meal time', max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = _('Meal')
        verbose_name_plural = _('Meals')
        ordering = ('-id',)

    @property
    def get_time(self):
        return self.time.strftime('%H:%M') if self.time else '-'

    def __str__(self) -> str:
        return f'{self.title} - {self.get_time}'


# Sports model
class Sport(models.Model):
    title = models.CharField('Title', max_length=128)

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
    

class TrainingProgram(models.Model):
    DAY_CHOICES = DayChoices

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


# DietFreeProgram model
class DietProgramFree(models.Model):
    DAY_CHOICES = DayChoices

    day = models.CharField(max_length=15, choices=DayChoices.choices, default=DayChoices.SATURDAY)
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, related_name='diet_program_free', null=True)
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


# DietProgram model(one program for each user)
class DietProgram(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'), related_name='diet_programs')
    title = models.CharField(_('Title'), max_length=64, help_text=_('example: program of first month'))

    created_at = models.DateTimeField('Create time', auto_now_add=True)
    modified_at = models.DateTimeField('Modify time', auto_now=True)

    class Meta:
        verbose_name = _("User's diet program")
        verbose_name_plural = _("User's diet programs")
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
    
    def __str__(self) -> str:
        user_phone = self.user.get_raw_phonenumber()
        return f'{user_phone} - {self.user.get_full_name()}'
    

# DailyDietProgram model
class DailyDietProgram(models.Model):
    DAY_CHOICES = DayChoices

    diet_program = models.ForeignKey(DietProgram, on_delete=models.CASCADE, verbose_name=_('User program'), related_name='daily_programs')
    day = models.CharField(_('Day of weak'), max_length=32, choices=DAY_CHOICES.choices)

    created_at = models.DateTimeField(_('Create time'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modify time'), auto_now=True)

    class Meta:
        verbose_name = _("User's daily program")
        verbose_name_plural = _("User's daily programs")
        ordering = ('-created_at',)

        constraints = [
            models.UniqueConstraint(fields=['diet_program', 'day'], name='unique_day_per_program')
        ]
    
    @property
    def get_day_label(self) -> str:
        return self.get_day_display()

    def __str__(self) -> str:
        return f'{self.diet_program} - {self.get_day_label}'


# Daily Diet Program Meals model
class DailyDietMeal(models.Model):
    daily_program = models.ForeignKey(DailyDietProgram, on_delete=models.CASCADE, verbose_name=_('Daily program'), related_name='daily_diet_meals')
    meal = models.ForeignKey(Meal, on_delete=models.PROTECT, verbose_name=_('Meal'), related_name='daily_meals')

    created_at = models.DateTimeField('Create time', auto_now_add=True)
    modified_at = models.DateTimeField('Modify time', auto_now=True)

    class Meta:
        verbose_name = _('Daily meal')
        verbose_name_plural = _('Daily meals')
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'{self.daily_program} - {self.meal}'
    

# Daily Meal Foods model
class MealFood(models.Model):
    daily_meal = models.ForeignKey(DailyDietMeal, on_delete=models.CASCADE, verbose_name=_('Daily meal'), related_name='meal_foods')
    food = models.ForeignKey(Food, on_delete=models.PROTECT, verbose_name=_('Food'), related_name='meal_foods')
    amount = models.PositiveBigIntegerField(_('Amount'), default=0)
    amount_unit = models.CharField(_('Amount unit'), max_length=128, null=True, blank=True, help_text=_('example: (gram, milligram, glass, ...)'))
    energy = models.PositiveBigIntegerField(_('Energy'), default=0)

    created_at = models.DateTimeField(_('Create time'), auto_now_add=True)
    modified_at = models.DateTimeField('Modify time', auto_now=True)

    class Meta:
        verbose_name = _("Meal's food")
        verbose_name_plural = _("Meal's foods")
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'{self.daily_meal} - {self.food.title}'


# General DietProgram's Recommends model
class DietRecommend(models.Model):
    diet_program = models.ForeignKey(DietProgram, on_delete=models.CASCADE, verbose_name=_('Diet Program'), related_name='recommends')
    text = models.CharField(_('Recommendation'), max_length=128)

    created_at = models.DateTimeField(_('Create time'), auto_now_add=True)

    class Meta:
        verbose_name = _('Recommend')
        verbose_name_plural = _('Recommends')
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'{self.diet_program} - {self.text[:16]}'