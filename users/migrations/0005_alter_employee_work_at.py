# Generated by Django 5.1 on 2024-08-11 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_employee_phone_number_employee_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='work_at',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.branch'),
        ),
    ]
