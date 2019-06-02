from wagtail.core import blocks
from . import constants

class AmenitiesBlock(blocks.StructBlock):
    amenity_type = blocks.ChoiceBlock(required=True, max_length=6, choices=constants.AMENITIES_CHOICES)
    location = blocks.CharBlock(required=True)
