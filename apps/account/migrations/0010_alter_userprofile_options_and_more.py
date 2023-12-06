# Generated by Django 4.2 on 2023-10-24 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_userprofile_create_time_userprofile_modified_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ('-id',), 'verbose_name': 'پروفایل کاربر', 'verbose_name_plural': 'پروفایل کاربران'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='additional_explain',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات تکمیلی'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='arm_size',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='سایز بازو'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='body_checkup',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/users/docs', verbose_name='آزمایش چکاپ بدن'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='body_composition',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/users/docs', verbose_name='آزمایش ترکیب بدنی'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='body_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/users/docs', verbose_name='تصویر بدن'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='breakfast_time',
            field=models.CharField(default='07:00', max_length=8, verbose_name='زمان ترجیحی صبحانه'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dinner_time',
            field=models.CharField(default='18:00', max_length=8, verbose_name='زمان ترجیحی شام'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='doing_exercise',
            field=models.CharField(default='تمرین ورزشی ندارم', max_length=64, verbose_name='انجام تمرین ورزشی'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='exercise_systems',
            field=models.TextField(blank=True, null=True, verbose_name='سیستم های تمرینی تجربه شده'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='family_disease',
            field=models.BooleanField(default=False, verbose_name='سابقه بیماری خانوادگی'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='goal_of_program',
            field=models.TextField(blank=True, null=True, verbose_name='هدف دریافت برنامه'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.PositiveIntegerField(default=0, verbose_name='قد'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='hip_size',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='سایز ران'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='in_diet',
            field=models.BooleanField(default=False, verbose_name='رژیم غذایی داشته/دارد'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_exercise',
            field=models.TextField(blank=True, null=True, verbose_name='آخرین زمان ورزش'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='launch_time',
            field=models.CharField(default='12:30', max_length=8, verbose_name='زمان ترجیجی ناهار'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='national_code',
            field=models.PositiveIntegerField(default=0, verbose_name='کد ملی'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='physical_damage',
            field=models.BooleanField(default=False, verbose_name='سابقه آسیب فیزیکی'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/users', verbose_name='تصویر کاربر'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='regular_exercise',
            field=models.BooleanField(default=False, verbose_name='سابقه تمرین منظم/حرفه ای'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='snack_time',
            field=models.CharField(default='10:00', max_length=8, verbose_name='زمان ترجیحی میان وعده'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='special_disease',
            field=models.BooleanField(default=False, verbose_name='دارای بیماری خاص'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='special_medicine',
            field=models.BooleanField(default=False, verbose_name='استفاده از داروی خاص'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='use_supplement',
            field=models.BooleanField(default=False, verbose_name='درحال مصرف مکمل ورزشی/غذایی'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='used_steroids',
            field=models.BooleanField(default=False, verbose_name='سابقه استفاده از داروی استروییدی'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='vegetarian',
            field=models.BooleanField(default=False, verbose_name='گیاه خوار'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='verified',
            field=models.BooleanField(default=False, verbose_name='تایید شده'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='waist_size',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='سایز کمر'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='want_supplement',
            field=models.BooleanField(default=False, verbose_name='خواستار مکمل ورزشی/غذایی'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.PositiveIntegerField(default=0, verbose_name='وزن'),
        ),
    ]