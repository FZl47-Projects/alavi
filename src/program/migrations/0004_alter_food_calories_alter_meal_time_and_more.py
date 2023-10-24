# Generated by Django 4.2 on 2023-10-23 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0003_alter_food_calories_alter_meal_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.PositiveIntegerField(default=0, help_text='کالری در هر واحد', verbose_name='کالری'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='time',
            field=models.TimeField(blank=True, help_text='مثال: 15:30', max_length=64, null=True, verbose_name='زمان وعده'),
        ),
        migrations.AlterField(
            model_name='mealfood',
            name='amount',
            field=models.PositiveIntegerField(default=0, verbose_name='مقدار'),
        ),
        migrations.AlterField(
            model_name='mealfood',
            name='energy',
            field=models.PositiveIntegerField(default=0, verbose_name='انرژی'),
        ),
    ]
