# Generated by Django 4.2 on 2023-10-22 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('-id',), 'verbose_name': 'کاربر', 'verbose_name_plural': 'Users'},
        ),
    ]