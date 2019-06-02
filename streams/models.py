from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from modelcluster.models import ClusterableModel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
)
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from django import forms


class Place(index.Indexed, ClusterableModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    details = models.TextField(null=False, blank=False, help_text="Add place details")
    duration_of_visit = models.DurationField(null=False,
                                             blank=False,
                                             default='00:05:00',
                                             verbose_name=('timeslot_duration'),
                                             help_text=('[DD] [HH:[MM:]]ss[.uuuuuu] format')
                                             )

    map_icon = models.ForeignKey(
         "wagtailimages.Image",
         null=True, blank=True,
         on_delete=models.SET_NULL,
         related_name="+")

    trip_types = ParentalManyToManyField('TripType', null=True, blank=False)
    location_tags = ParentalManyToManyField('LocationTag', null=True, blank=False)
    panels = [
        FieldPanel("name"),
        FieldPanel("details"),
        FieldPanel("duration_of_visit"),
        ImageChooserPanel("map_icon"),
        MultiFieldPanel([
            InlinePanel("place_images"),
        ], heading="Images" ),
         FieldPanel('trip_types', widget=forms.CheckboxSelectMultiple),
         FieldPanel('location_tags', widget=forms.CheckboxSelectMultiple),
    ]

    search_fields = [
        index.SearchField('name', partial_match=True),
    ]

    def __str__(self):
        return self.name

register_snippet(Place)

class PlaceImages(Orderable):
    place = ParentalKey('Place', related_name="place_images", null=False, blank=False)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True, blank=False, unique=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    panels = [
        ImageChooserPanel("image"),
    ]

class LocationTag(models.Model):
    tag = models.CharField(max_length=100, blank=False, null=False, help_text="location tag")

    panels = [
                FieldPanel("tag"),
            ]

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = "Location Tag"
        verbose_name_plural = "Location Tags"

register_snippet(LocationTag)

class TripType(models.Model):
    trip_type = models.CharField(max_length=100, blank=False, null=False, help_text="Trip type")

    panels = [
                FieldPanel("trip_type"),
            ]

    def __str__(self):
        return self.trip_type

    class Meta:
        verbose_name = "Trip Type"
        verbose_name_plural = "Trip Types"

register_snippet(TripType)

class FareTable(models.Model):
    AC = 'AC'
    NONAC = 'Non AC'
    FEATURE_CHOICES = (
        (AC, 'AC'),
        (NONAC, 'Non AC'),
    )
    vehicle_type = models.CharField(max_length=100, blank=False, null=False)
    model = models.CharField(max_length=100, blank=False, null=False)
    seater = models.PositiveSmallIntegerField(null=False,default=0)
    per_km_rate = models.PositiveSmallIntegerField(null=False,default=0)
    vehicle_feature = models.CharField(max_length=6,choices=FEATURE_CHOICES, default=AC)

    panels = [
                FieldPanel("vehicle_type"),
                FieldPanel("model"),
                FieldPanel("seater"),
                FieldPanel("per_km_rate"),
                FieldPanel("vehicle_feature"),
            ]

    def __str__(self):
        return self.vehicle_type

    class Meta:
        verbose_name = "Fare"
        verbose_name_plural = "Fares"

register_snippet(FareTable)
