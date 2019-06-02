# Generated by Django 2.1.8 on 2019-06-02 07:09

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailimages', '0001_squashed_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationTouristPlaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OnRouteTouristPlaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('distance_from_origin', models.IntegerField(default=0)),
                ('amenities', wagtail.core.fields.StreamField([('amenity', wagtail.core.blocks.StructBlock([('amenity_type', wagtail.core.blocks.ChoiceBlock(choices=[(1, 'Lodging'), (2, 'Petrol Pump'), (3, 'Eating Place')], max_length=6)), ('location', wagtail.core.blocks.CharBlock(required=True))]))], blank=True, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OutstationRoutePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('banner_title', models.CharField(max_length=100)),
                ('road_condition_rating', models.PositiveSmallIntegerField()),
                ('road_map', models.TextField(help_text='Add road map details')),
                ('best_time_to_visit', models.TextField(help_text='Add road map details')),
                ('alternate_routes', models.TextField(help_text='Add alternate route details')),
                ('road_condition', models.TextField(help_text='Add road condition details')),
                ('total_distance', models.PositiveSmallIntegerField()),
                ('banner_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
