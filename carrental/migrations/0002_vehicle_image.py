# Generated by Django 5.0.4 on 2024-05-23 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='locations/%Y/%m/%D'),
        ),
    ]
