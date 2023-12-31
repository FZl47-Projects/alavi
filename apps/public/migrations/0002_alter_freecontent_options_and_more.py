# Generated by Django 4.2 on 2023-12-26 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='freecontent',
            options={'ordering': ('-id',), 'verbose_name': 'محتوای رایگان', 'verbose_name_plural': 'محتواهای رایگان'},
        ),
        migrations.AlterField(
            model_name='freecontent',
            name='short_description',
            field=models.CharField(help_text='تاریخ، اطلاعات اضافه و...', max_length=64, verbose_name='توضیح کوتاه'),
        ),
        migrations.AlterField(
            model_name='freecontent',
            name='title',
            field=models.CharField(default='بدون عنوان', max_length=64, verbose_name='عنوان محتوا'),
        ),
    ]
