# Generated by Django 4.0.6 on 2023-06-19 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0009_remove_hostel_fee_food_mess_fee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mess_fee',
            old_name='student_id',
            new_name='student',
        ),
    ]
