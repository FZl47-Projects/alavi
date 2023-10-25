# Generated by Django 4.2 on 2023-10-24 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_userprofile_arm_size_alter_userprofile_height_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('0', 'شنبه'), ('1', 'یکشنبه'), ('2', 'دوشنبه'), ('3', 'سه شنبه'), ('4', 'چهارشنبه'), ('5', 'پنجشنبه'), ('6', 'جمعه')], max_length=16, verbose_name='روز هفته')),
            ],
            options={
                'verbose_name': 'Exercise day',
                'verbose_name_plural': 'Exercise days',
                'ordering': ('id',),
            },
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='body_checkup',
            field=models.ImageField(blank=True, null=True, upload_to='images/users/docs', verbose_name='آزمایش چکاپ بدن'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='body_composition',
            field=models.ImageField(blank=True, null=True, upload_to='images/users/docs', verbose_name='آزمایش ترکیب بدنی'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='body_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/users/docs', verbose_name='تصویر بدن'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='exercise_days',
            field=models.ManyToManyField(related_name='user_profile', to='account.exerciseday', verbose_name='Exercise days willing'),
        ),
    ]