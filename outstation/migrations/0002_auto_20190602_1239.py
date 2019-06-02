# Generated by Django 2.1.8 on 2019-06-02 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('outstation', '0001_initial'),
        ('streams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='outstationroutepage',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='route_destination', to='streams.Place'),
        ),
        migrations.AddField(
            model_name='outstationroutepage',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='outstationroutepage',
            name='origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='route_origin', to='streams.Place'),
        ),
        migrations.AddField(
            model_name='onroutetouristplaces',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='on_route_places', to='outstation.OutstationRoutePage'),
        ),
        migrations.AddField(
            model_name='onroutetouristplaces',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='streams.Place'),
        ),
        migrations.AddField(
            model_name='destinationtouristplaces',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_places', to='outstation.OutstationRoutePage'),
        ),
        migrations.AddField(
            model_name='destinationtouristplaces',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='streams.Place'),
        ),
    ]
