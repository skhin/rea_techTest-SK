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
           "get_image",
           "get_thumbnail" 
        )