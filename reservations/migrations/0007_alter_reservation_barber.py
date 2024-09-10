# Generated by Django 5.1 on 2024-09-10 14:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0006_service_is_highlighted'),
        ('users', '0009_remove_customer_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='barber',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.employee'),
        ),
    ]
