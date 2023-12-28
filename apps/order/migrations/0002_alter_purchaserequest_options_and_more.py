# Generated by Django 4.2 on 2023-12-28 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchaserequest',
            options={'verbose_name': 'درخواست خرید', 'verbose_name_plural': 'درخواست\u200cهای خرید'},
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='package',
            field=models.ManyToManyField(related_name='purchase_requests', to='package.package', verbose_name='پکیج ها'),
        ),
    ]