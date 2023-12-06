from django.utils.translation import gettext as _
from .enums import WorkoutLevelChoices, WeekChoices
from apps.core.utils import get_timesince_persian
from django.shortcuts import reverse
from apps.diet.enums import DayChoices
from apps.account.models import User
from django.db import models


# Workouts model
class Workout(models.Model):
    WORKOUT_LEVELS = WorkoutLevelChoices

    title = models.CharField(_('Workout title'), max_length=64)
    level = models.CharField(_('Level (optional)'), max_length=32, choices=WORKOUT_LEVELS.choices, null=True, blank=True)

    class Meta:
        verbose_name = _('Workout')
        verbose_name_plural = _('Workouts')

    def __str__(self) -> str:
        return self.title


# ExercisePrograms model
class ExerciseProgram(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'), related_name='exercise_programs')
    title = models.CharField(_('Title'), max_length=64, help_text=_('example: exercise program of first month'))

    created_at = models.DateTimeField(_('Create time'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modify time'), auto_now=True)

    class Meta:
        verbose_name = _('Exercise program')
        verbose_name_plural = _('Exercise programs')

    def get_created_at(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M')

    def get_created_at_time_past(self):
        return get_timesince_persian(self.created_at)

    def get_weekly_programs(self):
        return self.weekly_programs.all()

    def get_absolute_url(self):
        return reverse('admin:exercise_exerciseprogram_change', args=(self.id,))

    def __str__(self) -> str:
        return f'{self.user} - {self.title}'


# WeeklyExercisePrograms models
class WeeklyExerciseProgram(models.Model):
    WEEKS = WeekChoices

    exercise_program = models.ForeignKey(ExerciseProgram, on_delete=models.CASCADE, verbose_name=_('Exercise program'), related_name='weekly_programs')
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
            models.UniqueConstraint(fields=['exercise_program', 'week'], name='unique_week_per_exercise_program')
        ]

    @property
    def get_week_label(self):
        return self.get_week_display()

    def get_absolute_url(self):
        return reverse('admin:exercise_weeklyexerciseprogram_change', args=(self.id,))

    def __str__(self) -> str:
        return f'{self.exercise_program} - {self.get_week_label}'


# DailyExercisePrograms model
class DailyExerciseProgram(models.Model):
    DAYS = DayChoices

    weekly_program = models.ForeignKey(WeeklyExerciseProgram, on_delete=models.CASCADE, verbose_name=_('Weekly program'), related_name='daily_programs')
    day = models.CharField(_('Day of week'), max_length=16, choices=DAYS.choices, default=DAYS.SATURDAY)

    created_at = models.DateTimeField(_('Create time'), auto_now_add=True)

    class Meta:
        verbose_name = _('Daily program')
        verbose_name_plural = _('Daily programs')
        ordering = ('day',)

        constraints = [
            models.UniqueConstraint(fields=['weekly_program', 'day'], name='unique_day_per_daily_program')
        ]

    def get_day_label(self):
        return self.get_day_display()

    def get_absolute_url(self):
        return reverse('admin:exercise_dailyexerciseprogram_change', args=(self.id,))

    def __str__(self) -> str:
        return f'{self.weekly_program.get_week_label} - {self.get_day_label()}'


# Exercises model
class Exercise(models.Model):
    daily_program = models.ForeignKey(DailyExerciseProgram, on_delete=models.CASCADE, verbose_name=_('Daily program'), related_name='exercises')
    workout = models.ForeignKey(Workout, on_delete=models.PROTECT, verbose_name=_('Workout'), related_name='exercises')
    sets = models.PositiveBigIntegerField(_('Sets'), default=1)
    number = models.PositiveBigIntegerField(_('Numbers in a set'), default=1)
    rest = models.PositiveBigIntegerField(_('Rest time (Seconds)'), default=20)

    created_at = models.DateTimeField(_('Create time'), auto_now_add=True)

    class Meta:
        verbose_name = _('Exercise')
        verbose_name_plural = _('Exercise')

    def __str__(self) -> str:
        return f'{self.workout.title[:14]}'


# ExerciseRecommends model
class ExerciseRecommend(models.Model):
    exercise_program = models.ForeignKey(ExerciseProgram, on_delete=models.CASCADE, verbose_name=_('Exercise program'), related_name='recommends')
    text = models.CharField(_('Recommendation'), max_length=128)

    class Meta:
        verbose_name = _('Exercise recommend')
        verbose_name_plural = _('Exercise recommends')
        ordering = ('id',)

    def __str__(self) -> str:
        return f'{self.exercise_program} - {self.text[:10]}'
