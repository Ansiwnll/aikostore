# Generated by Django 3.0.7 on 2023-12-18 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_auto_20231218_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='state',
            field=models.CharField(choices=[('Жезказган', 'Qazaqstan')], max_length=100),
        ),
    ]