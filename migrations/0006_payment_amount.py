# Generated by Django 4.0.6 on 2023-06-09 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0005_rename_o_id_leave_l_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
