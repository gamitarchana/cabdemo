# Generated by Django 2.1.8 on 2019-06-02 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0002_auto_20190602_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='duration_of_visit',
            field=models.DurationField(default='00:05:00', help_text='[DD] [HH:[MM:]]ss[.uuuuuu] format', verbose_name='timeslot_duration'),
        ),
    ]
