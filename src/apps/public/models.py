from django.utils.translation import gettext as _
from django.shortcuts import reverse
from django.db import models
from apps.exercise.enums import WeekChoices
from apps.program.enums import DayChoices
from apps.program.models import Meal, Food
from apps.exercise.models import Workout


# Certificates model
class Certificate(models.Model):
    title = models.CharField(_('Certificate title'), max_length=64, null=True, blank=True, help_text=_('Optional'))
    picture = models.ImageField(_('Picture'), upload_to='images/certificates')

    class Meta:
        verbose_name = _('Certificate')
        verbose_name_plural = _('Certificates')


# Start Models related to free exercise program
# FreeExercisePrograms model
class FreeExerciseProgram(models.Model):
    is_active = models.BooleanField(_('Active'), default=True)

    created_at = models.DateTimeField(_('Create time'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modify time'), auto_now=True)

    class Meta:
        verbose_name = _('Free exercise program')
        verbose_name_plural = _('Free exercise programs')

    def get_created_at(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M')

    def get_weekly_programs(self):
        return self.free_weekly_exercises.all()

    def get_absolute_url(self):
        return reverse('admin:public_freeexerciseprogram_change', args=(self.id,))

    def __str__(self) -> str:
        return f'{_("Free exercise program")} - {self.id}'


# FreeWeeklyExercise model
class FreeWeeklyExercise(models.Model):
    WEEKS = WeekChoices

    exercise_program = models.ForeignKey(FreeExerciseProgram, on_delete=models.CASCADE, verbose_name=_('Exercise program'), related_name='free_weekly_exercises')
    week = models.CharField(_('Week'), max_length=32, choices=WEEKS.choices)
    warm_up = models.CharField(_('Warm up time (Minute)'), max_length=16, null=True, blank=True, help_text=_('example: 5 - 10'))
    cool_down = models.CharField(_('Cool down time (Minute)'), max_length=16, null=True, blank=True, help_text=_('example: 5 - 10'))

    created_at = models.DateTimeField(_('Create time'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modify time'), auto_now=True)

    class Meta:
        verbose_name = _('Weekly program')
        verbose_name_plural = _('Weekly programs')
        ordering = ('week',)

        constraints = [
            models.UniqueConstraint(fields=['exercise_program', 'week'], name='unique_week_per_free_exercise_program')
        ]

    @property
    def get_week_label(self):
        return self.get_week_display()

    def get_absolute_url(self):
        return reverse('admin:public_freeweeklyexercise_change', args=(self.id,))

    def __str__(self) -> str:
        return f'{self.exercise_program} - {self.get_week_label}'


# FreeDailyExercise model
class FreeDailyExercise(models.Model):
    DAYS = DayChoices

    weekly_program = models.ForeignKey(FreeWeeklyExercise, on_delete=models.CASCADE, verbose_name=_('Weekly program'), related_name='free_daily_exercises')
    day = models.CharField(_('Day of week'), max_length=16, choices=DAYS.choices, default=DAYS.SATURDAY)

    created_at = models.DateTimeField(_('Create time'), auto_now_add=True)

    class Meta:
        verbose_name = _('Daily program')
        verbose_name_plural = _('Daily programs')
        ordering = ('day',)

        constraints = [
            models.UniqueConstraint(fields=['weekly_program', 'day'], name='unique_day_per_free_weekly_exercise')
        ]

    def get_day_label(self):
        return self.get_day_display()

    def get_absolute_url(self):
        return reverse('admin:public_freedailyexercise_change', args=(self.id,))

    def __str__(self) -> str:
        return f'{self.weekly_program.get_week_label} - {self.get_day_label()}'


# FreeExercises model
class FreeExercise(models.Model):
    daily_program = models.ForeignKey(FreeDailyExercise, on_delete=models.CASCADE, verbose_name=_('Daily program'), related_name='free_exercises')
    workout = models.ForeignKey(Workout, on_delete=models.PROTECT, verbose_name=_('Workout'), related_name='free_exercises')
    sets = models.PositiveBigIntegerField(_('Sets'), default=1)
    number = models.PositiveBigIntegerField(_('Numbers in a set'), default=1)
    rest = models.PositiveBigIntegerField(_('Rest time (Seconds)'), default=20)

    created_at = models.DateTimeField(_('Create time'), auto_now_add=True)

    class Meta:
        verbose_name = _('Exercise')
        verbose_name_plural = _('Exercise')

    def __str__(self) -> str:
        return f'{self.workout.title[:14]}'


# Start Models related to free diet program
# FreeDietProgram model
class FreeDietProgram(models.Model):
    is_active = models.BooleanField(_('Active'), default=True)

    created_at = models.DateTimeField(_('Create time'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modify time'), auto_now=True)

    class Meta:
        verbose_name = _('Free diet program')
        verbose_name_plural = _('Free diet programs')
        ordering = ('id',)

    def get_created_at(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M')

    def get_daily_programs(self):
        return self.free_daily_diet_programs.all()

    def get_absolute_url(self):
        return reverse('admin:public_freedietprogram_change', args=(self.id,))

    def __str__(self) -> str:
        return f'{_("Free diet program")} - {self.id}'


# FreeDailyDietPrograms model
class FreeDailyDietProgram(models.Model):
    DAYS = DayChoices

    diet_program = models.ForeignKey(FreeDietProgram, on_delete=models.CASCADE, verbose_name=_('Diet program'), related_name='free_daily_diet_programs')
    day = models.CharField(_('Day'), max_length=8, choices=DAYS.choices, default=DAYS.SATURDAY)

    class Meta:
        verbose_name = _('Daily program')
        verbose_name_plural = _('Daily programs')
        ordering = ('day',)

        constraints = [
            models.UniqueConstraint(fields=['diet_program', 'day'], name='unique_day_per_free_program')
        ]

    def get_day_label(self):
        return self.get_day_display()

    def get_absolute_url(self):
        return reverse('admin:public_freedailydietprogram_change', args=(self.id,))

    def __str__(self) -> str:
        return f'{self.diet_program} - {self.get_day_label()}'


# FreeDietMeals model
class FreeDietMeal(models.Model):
    daily_program = models.ForeignKey(FreeDailyDietProgram, on_delete=models.CASCADE, verbose_name=_('Daily program'), related_name='free_diet_meals')
    meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True, verbose_name=_('Meal'), related_name='free_diet_meals')

    class Meta:
        verbose_name = _('Diet meal')
        verbose_name_plural = _('Diet meals')
        ordering = ('meal__time',)

    def get_absolute_url(self):
        return reverse('admin:public_freedietmeal_change', args=(self.id,))

    def __str__(self) -> str:
        return f'{self.daily_program.get_day_label()} - {self.meal.title}'


# FreeMealFoods model
class FreeMealFood(models.Model):
    diet_meal = models.ForeignKey(FreeDietMeal, on_delete=models.CASCADE, verbose_name=_('Diet meal'), related_name='free_meal_foods')
    food = models.ForeignKey(Food, on_delete=models.PROTECT, verbose_name=_('Food'), related_name='free_meal_foods')
    amount = models.PositiveBigIntegerField(_('Amount'), default=0)
    amount_unit = models.CharField(_('Amount unit'), max_length=128, null=True, blank=True, help_text=_('example: (gram, milligram, glass, ...)'))
    energy = models.PositiveBigIntegerField(_('Energy'), default=0)

    created_at = models.DateTimeField(_('Create time'), auto_now_add=True)
    modified_at = models.DateTimeField('Modify time', auto_now=True)

    class Meta:
        verbose_name = _("Meal's food")
        verbose_name_plural = _("Meal's foods")
        ordering = ('created_at',)

    def __str__(self) -> str:
        return f'{self.diet_meal} - {self.food.title}'
