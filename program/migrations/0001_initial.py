# Generated by Django 4.1.3 on 2023-10-19 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DietMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('time', models.TimeField(blank=True, max_length=64, null=True, verbose_name='Meal Time')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modify time')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=128, verbose_name='Title')),
                ('calories', models.PositiveIntegerField(default=0, verbose_name='Calories')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=128, verbose_name='Title')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='TrainingProgramCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modify time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training_program_category', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='TrainingProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('0', 'شنبه'), ('1', 'یکشنبه'), ('2', 'دوشنبه'), ('3', 'سه شنبه'), ('4', 'چهارشنبه'), ('5', 'پنجشنبه'), ('6', 'جمعه')], default='0', max_length=15)),
                ('rep', models.PositiveIntegerField(default=0, verbose_name='Repeat')),
                ('sets', models.PositiveIntegerField(default=0, verbose_name='Set')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modify time')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training_program_object', to='program.trainingprogramcategory')),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sport_training_programs', to='program.sport')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_training_program', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='DietProgramFree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('0', 'شنبه'), ('1', 'یکشنبه'), ('2', 'دوشنبه'), ('3', 'سه شنبه'), ('4', 'چهارشنبه'), ('5', 'پنجشنبه'), ('6', 'جمعه')], default='0', max_length=15)),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='amount')),
                ('energy', models.PositiveIntegerField(default=0, verbose_name='Energy')),
                ('description', models.TextField(null=True, verbose_name='Information')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modify time')),
                ('food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='food_diet_programs_free', to='program.food')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='DietProgramCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modify time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diet_program_category', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='DietProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('0', 'شنبه'), ('1', 'یکشنبه'), ('2', 'دوشنبه'), ('3', 'سه شنبه'), ('4', 'چهارشنبه'), ('5', 'پنجشنبه'), ('6', 'جمعه')], default='0', max_length=15)),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='amount')),
                ('energy', models.PositiveIntegerField(default=0, verbose_name='Energy')),
                ('description', models.TextField(null=True, verbose_name='Information')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modify time')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diet_program_object', to='program.dietprogramcategory')),
                ('food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='food_diet_programs', to='program.food')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_diet_program', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
