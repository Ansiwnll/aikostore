# Generated by Django 3.0.7 on 2023-12-20 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_auto_20231220_0117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='status',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='address',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='email',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='order_date',
        ),
        migrations.AlterField(
            model_name='orders',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.Car'),
        ),
    ]
