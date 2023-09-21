# Generated by Django 4.1.3 on 2023-09-21 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0010_remove_diet_program_object_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diet_program_object',
            name='info',
        ),
        migrations.RemoveField(
            model_name='training_program_object',
            name='info',
        ),
        migrations.AddField(
            model_name='diet_program_object',
            name='description',
            field=models.TextField(null=True, verbose_name='Information'),
        ),
        migrations.AddField(
            model_name='training_program_object',
            name='description',
            field=models.TextField(null=True, verbose_name='Information'),
        ),
    ]
