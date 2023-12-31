# Generated by Django 4.2 on 2023-12-25 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('diet', 'رژیم غذایی'), ('workout', 'بدنسازی'), ('crossfit', 'کراسفیت'), ('workout_diet', 'بدنسازی + رژیم غذایی'), ('crossfit_diet', 'کراسفیت + رژیم غذایی'), ('private_workout_diet', 'بدنسازی خصوصی'), ('any_diet', 'هر ورزش تخصصی'), ('offline', 'آفلاین')], default='diet', max_length=128, verbose_name='نوع پکیج')),
                ('price', models.IntegerField(default=0, help_text='ریال', verbose_name='قیمت')),
                ('buy_link', models.URLField(blank=True, null=True, verbose_name='لینک خرید')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/packages/icons', verbose_name='آیکون پکیج')),
                ('fw_class', models.CharField(blank=True, max_length=64, null=True, verbose_name='CSS class (FontAwesome)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')),
            ],
            options={
                'verbose_name': 'پکیج',
                'verbose_name_plural': 'پکیج ها',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='PackageInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='متن')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_info', to='package.package', verbose_name='پکیج')),
            ],
            options={
                'verbose_name': 'توضیح پکیج',
                'verbose_name_plural': 'توضیحات پکیج',
            },
        ),
    ]
