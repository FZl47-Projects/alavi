# Generated by Django 4.2 on 2023-10-22 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('diet', 'رژیم غذایی'), ('exercise', 'ورزش'), ('crossfit', 'Crossfit'), ('exercise_diet', 'Exercise + Diet'), ('crossfit_diet', 'Crossfit + Diet'), ('any_diet', 'Any sport + Diet'), ('offline', 'Offline')], default='diet', max_length=128, verbose_name='Package type')),
                ('price', models.IntegerField(default=0, help_text='Rials', verbose_name='Price')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')),
            ],
            options={
                'verbose_name': 'Package',
                'verbose_name_plural': 'Packages',
                'ordering': ('id',),
            },
        ),
    ]