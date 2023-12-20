# Generated by Django 3.0.7 on 2023-12-19 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0014_auto_20231220_0112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='Car',
            new_name='car',
        ),
        migrations.AddField(
            model_name='car',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Order Confirmed', 'Order Confirmed'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered')], max_length=50, null=True),
        ),
    ]