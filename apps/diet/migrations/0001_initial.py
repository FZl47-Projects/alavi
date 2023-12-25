# Generated by Django 4.2 on 2023-12-25 16:46

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
            name='DailyDietMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modify time')),
            ],
            options={
                'verbose_name': 'وعده روزانه',
                'verbose_name_plural': 'وعده های روزانه',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='DietProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='مثال: برنامه ماه اول', max_length=64, verbose_name='عنوان')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modify time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diet_programs', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'برنامه غذایی کاربر',
                'verbose_name_plural': 'برنامه های غذایی کاربران',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='عنوان غذا')),
                ('calories', models.PositiveIntegerField(default=0, help_text='کالری در هر واحد', verbose_name='کالری')),
            ],
            options={
                'verbose_name': 'غذا',
                'verbose_name_plural': 'غذاها',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='عنوان وعده')),
                ('time', models.TimeField(blank=True, help_text='مثال: 15:30', max_length=64, null=True, verbose_name='زمان وعده')),
            ],
            options={
                'verbose_name': 'وعده',
                'verbose_name_plural': 'وعده ها',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='MealFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='مقدار')),
                ('amount_unit', models.CharField(blank=True, help_text='مثال: گرم، میلی گرم، لیوان و...', max_length=128, null=True, verbose_name='واحد مقدار')),
                ('energy', models.PositiveIntegerField(default=0, verbose_name='انرژی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modify time')),
                ('daily_meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_foods', to='diet.dailydietmeal', verbose_name='وعده روزانه')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='meal_foods', to='diet.food', verbose_name='غذا')),
            ],
            options={
                'verbose_name': 'غذای وعده',
                'verbose_name_plural': 'غذاهای وعده',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='DietRecommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128, verbose_name='توصیه')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('diet_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommends', to='diet.dietprogram', verbose_name='برنامه غذایی')),
            ],
            options={
                'verbose_name': 'توصیه',
                'verbose_name_plural': 'توصیه ها',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='DailyDietProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('0', 'شنبه'), ('1', 'یکشنبه'), ('2', 'دوشنبه'), ('3', 'سه شنبه'), ('4', 'چهارشنبه'), ('5', 'پنجشنبه'), ('6', 'جمعه')], max_length=32, verbose_name='روز هفته')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')),
                ('diet_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_programs', to='diet.dietprogram', verbose_name='برنامه کاربر')),
            ],
            options={
                'verbose_name': 'برنامه روزانه',
                'verbose_name_plural': 'برنامه های روزانه کابر',
                'ordering': ('day',),
            },
        ),
        migrations.AddField(
            model_name='dailydietmeal',
            name='daily_program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_diet_meals', to='diet.dailydietprogram', verbose_name='برنامه روزانه'),
        ),
        migrations.AddField(
            model_name='dailydietmeal',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='daily_meals', to='diet.meal', verbose_name='وعده'),
        ),
        migrations.AddConstraint(
            model_name='dailydietprogram',
            constraint=models.UniqueConstraint(fields=('diet_program', 'day'), name='unique_day_per_program'),
        ),
    ]
