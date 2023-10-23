from django.utils.translation import gettext as _
from django.db import models

from program.enums import DayChoices
from program.models import Meal, Food


# Certificates model
class Certificate(models.Model):
    title = models.CharField(_('Certificate title'), max_length=64, null=True, blank=True, help_text=_('Optional'))
    picture = models.ImageField(_('Picture'), upload_to='images/certificates')

    class Meta:
        verbose_name = _('Certificate')
        verbose_name_plural = _('Certificates')


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
