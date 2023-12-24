# Generated by Django 4.2 on 2023-12-24 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_alter_userprofile_body_checkup_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='exercise_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Exercise name'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='family_disease_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Family disease name'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='special_disease_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Special disease name'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='steroids_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Steroid medicine name'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='supplement_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Supplement name'),
        ),
    ]