# Generated by Django 4.0.6 on 2022-07-23 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bm', '0005_remove_appointment_massage'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bm.category', verbose_name='Appointment category'),
        ),
    ]
