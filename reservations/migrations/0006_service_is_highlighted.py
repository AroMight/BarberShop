# Generated by Django 5.1 on 2024-09-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_alter_reservation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='is_highlighted',
            field=models.BooleanField(default=False),
        ),
    ]
