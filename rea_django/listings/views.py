from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ListingsSerializer
from .models import Listings

class LatestListingsList(APIView):
    def get(self, request, format=None):
        listings = Listings.objects.all()[0:6]
        serializer = ListingsSerializer(listings, many=True)
        return Response(serializer.data)

class ListingsDetail(APIView):
    def get_listings(self, country_slug, listings_slug):
        try:
            return Listings.objects.filter(country__slug=country_slug).get(slug=listings_slug)
        except Listings.DoesNotExist:
            raise Http404
    
    def get(self, request, country_slug, listings_slug, format=None):
        listings = self.get_listings(country_slug, listings_slug)
        serializer = ListingsSerializer(listings)
        return Response(serializer.data)


