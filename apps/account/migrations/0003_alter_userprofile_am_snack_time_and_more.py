# Generated by Django 4.2 on 2023-12-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_userprofile_snack_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='am_snack_time',
            field=models.CharField(default='-', max_length=8, verbose_name='زمان ترجیحی میان وعده(قبل از ظهر)'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='doing_exercise',
            field=models.CharField(default='تمرین ورزشی ندارم', max_length=64, verbose_name='وضعیت انجام تمرین ورزشی'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='exercise_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='عنوان تمرین منظم/حرفه\u200cای'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pm_snack_time',
            field=models.CharField(default='-', max_length=8, verbose_name='زمان ترجیحی میان وعده(بعد از ظهر)'),
        ),
    ]
