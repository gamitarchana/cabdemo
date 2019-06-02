# Generated by Django 2.1.8 on 2019-06-02 09:50

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('outstation', '0003_auto_20190602_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onroutetouristplaces',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='on_route_places', to='outstation.OutstationRoutePage'),
        ),
        migrations.AlterField(
            model_name='onroutetouristplaces',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='streams.Place', unique=True),
        ),
    ]
