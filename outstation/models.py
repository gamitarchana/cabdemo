from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
    MultiFieldPanel,
    InlinePanel,
)
from wagtail.api import APIField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from modelcluster.fields import ParentalKey
from django.conf import settings
from django.contrib.auth.models import User
from streams import blocks
from streams import constants
from streams.models import LocationTag, TripType, FareTable, Place
from streams.serializers import PlaceSerializer, PlaceListSerializer
from wagtail.snippets.edit_handlers import SnippetChooserPanel

# Create your models here.

class OutstationRoutePage(Page):
    template="outstation/outstation_route_page.html"

    banner_title=models.CharField(max_length=100, null=False)
    banner_image=models.ForeignKey(
        "wagtailimages.Image",
        null=True, blank=False,
        on_delete=models.SET_NULL,
        related_name="+")

    origin = models.ForeignKey(
        "streams.Place",
        null=True,
        on_delete=models.SET_NULL,
        related_name="route_origin")

    destination = models.ForeignKey(
        "streams.Place",
        null=True,
        on_delete=models.SET_NULL,
        related_name="route_destination")


    road_condition_rating = models.PositiveSmallIntegerField()
    road_map = models.TextField(null=False, help_text="Add road map details")
    best_time_to_visit = models.TextField(null=False, help_text="Add road map details")
    alternate_routes = models.TextField(null=False, help_text="Add alternate route details")
    road_condition = models.TextField(null=False, help_text="Add road condition details")

    total_distance = models.PositiveSmallIntegerField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    api_fields = [
        APIField("banner_title"),
        APIField("banner_image"),
        APIField("origin", serializer = PlaceSerializer()),
        APIField("destination", serializer = PlaceSerializer()),
        APIField("on_route_places", serializer = PlaceListSerializer()),
        APIField("destination_places", serializer = PlaceListSerializer()),
        APIField("road_condition_rating"),
        APIField("road_map"),
        APIField("best_time_to_visit"),
        APIField("alternate_routes"),
        APIField("road_condition"),
        APIField("total_distance"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        ImageChooserPanel("banner_image"),
        SnippetChooserPanel('origin'),
        SnippetChooserPanel('destination'),
        MultiFieldPanel([
            InlinePanel("on_route_places"),
        ], heading="On Route Places" ),
        MultiFieldPanel([
            InlinePanel("destination_places"),
        ], heading="Destination Tourist Places" ),
        FieldPanel("road_condition_rating"),
        FieldPanel("road_map"),
        FieldPanel("best_time_to_visit"),
        FieldPanel("alternate_routes"),
        FieldPanel("road_condition"),
        FieldPanel("total_distance"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        location_tags = LocationTag.objects.all()
        context["location_tags"] = location_tags

        trip_types = TripType.objects.all()
        context["trip_types"] = trip_types

        fare_table = FareTable.objects.all()
        context["fare_table"] = fare_table

        context["total_likes"] = self.total_likes()

        context["total_reviews"] = self.total_reviews()

        context["AMENITIES"] = constants.AMENITIES

        context["data_api"] = settings.REST_API_ENDPOINT

        return context

    def total_likes(self):
        return self.likes.count()

    def total_reviews(self):
        return self.page_review.count()

class OnRouteTouristPlaces(Orderable):
    page = ParentalKey("outstation.OutstationRoutePage", related_name="on_route_places", null=False, blank=False)
    place = models.ForeignKey(
        "streams.Place",
        null=True, unique=True,
        on_delete=models.SET_NULL,
        related_name="+")
    distance_from_origin = models.IntegerField(null=False, default=0)
    amenities = StreamField(
         [
            ("amenity", blocks.AmenitiesBlock()),
        ],
        null=True,
        blank=True
    )
    panels = [
        SnippetChooserPanel("place"),
        FieldPanel("distance_from_origin"),
        StreamFieldPanel("amenities"),
    ]


class DestinationTouristPlaces(Orderable):
    page = ParentalKey("outstation.OutstationRoutePage", related_name="destination_places", null=False, blank=False)
    place = models.ForeignKey(
        "streams.Place",
        null=True, unique=True,
        on_delete=models.SET_NULL,
        related_name="+")
    panels = [
        SnippetChooserPanel("place"),
    ]
