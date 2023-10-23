# Generated by Django 4.2 on 2023-10-22 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0003_alter_package_options_alter_package_price_and_more'),
        ('account', '0005_user_packages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('-id',), 'verbose_name': 'کاربر', 'verbose_name_plural': 'کاربران'},
        ),
        migrations.AlterField(
            model_name='user',
            name='packages',
            field=models.ManyToManyField(blank=True, null=True, related_name='users', to='package.package', verbose_name='پکیج ها'),
        ),
    ]