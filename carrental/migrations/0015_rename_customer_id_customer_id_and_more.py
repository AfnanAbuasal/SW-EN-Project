# Generated by Django 5.0.4 on 2024-05-24 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0014_alter_vehicle_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='lessor',
            old_name='lessor_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='renting',
            old_name='rent_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='vehicle_id',
            new_name='id',
        ),
    ]
