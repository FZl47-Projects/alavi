# Generated by Django 4.2 on 2023-10-24 10:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_userprofile_delete_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='زمان ایجاد'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='modified_time',
            field=models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش'),
        ),
    ]
