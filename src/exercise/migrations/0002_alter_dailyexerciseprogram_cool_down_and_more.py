# Generated by Django 4.1.3 on 2023-10-21 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyexerciseprogram',
            name='cool_down',
            field=models.CharField(help_text='مثال: 5 - 10', max_length=16, verbose_name='زمان سرد کردن (دقیقه)'),
        ),
        migrations.AlterField(
            model_name='dailyexerciseprogram',
            name='warm_up',
            field=models.CharField(help_text='مثال: 5 - 10', max_length=16, verbose_name='زمان گرم کردن (دقیقه)'),
        ),
    ]