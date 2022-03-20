from rest_framework import serializers
from .models import Country, Listings

class ListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listings
        fields = (
           "id",
           "name",
           "get_absolute_url",
           "description",
           "price",
        #    "percentage",
           "get_image",
           "get_thumbnail" 
        )

class CountrySerializer(serializers.ModelSerializer):
    listings = ListingsSerializer(many=True)

    class Meta:
        model = Country
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "listings"
        )