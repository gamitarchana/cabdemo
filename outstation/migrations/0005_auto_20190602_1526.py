# Generated by Django 2.1.8 on 2019-06-02 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outstation', '0004_auto_20190602_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinationtouristplaces',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='streams.Place', unique=True),
        ),
    ]