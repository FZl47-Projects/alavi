# Generated by Django 4.1.3 on 2023-09-21 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0012_alter_diet_program_object_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet_program_object',
            name='day',
            field=models.CharField(choices=[('0', 'شنبه'), ('1', 'یکشنبه'), ('2', 'دوشنبه'), ('3', 'سه شنبه'), ('4', 'چهارشنبه'), ('5', 'پنجشنبه'), ('6', 'جمعه')], max_length=15),
        ),
        migrations.AlterField(
            model_name='training_program_object',
            name='day',
            field=models.CharField(choices=[('0', 'شنبه'), ('1', 'یکشنبه'), ('2', 'دوشنبه'), ('3', 'سه شنبه'), ('4', 'چهارشنبه'), ('5', 'پنجشنبه'), ('6', 'جمعه')], max_length=15),
        ),
        migrations.DeleteModel(
            name='Day',
        ),
    ]