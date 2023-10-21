# Generated by Django 4.1.3 on 2023-10-21 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_rename_weakly_program_dailyexerciseprogram_weekly_program_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyexerciseprogram',
            name='cool_down',
        ),
        migrations.RemoveField(
            model_name='dailyexerciseprogram',
            name='warm_up',
        ),
        migrations.AddField(
            model_name='weeklyexerciseprogram',
            name='cool_down',
            field=models.CharField(blank=True, help_text='مثال: 5 - 10', max_length=16, null=True, verbose_name='زمان سرد کردن (دقیقه)'),
        ),
        migrations.AddField(
            model_name='weeklyexerciseprogram',
            name='warm_up',
            field=models.CharField(blank=True, help_text='مثال: 5 - 10', max_length=16, null=True, verbose_name='زمان گرم کردن (دقیقه)'),
        ),
    ]
