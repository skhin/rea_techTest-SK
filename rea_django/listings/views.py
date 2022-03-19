from django.http import Http404
from django.db.models import Q
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ListingsSerializer, CountrySerializer
from .models import Country, Listings

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


class CountryDetail(APIView):
     def get_listings(self, country_slug):
        try:
            return Country.objects.get(slug=country_slug)
        except Listings.DoesNotExist:
            raise Http404
    
     def get(self, request, country_slug, format=None):
        country = self.get_listings(country_slug)
        serializer = CountrySerializer(country)
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        listings = Listings.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ListingsSerializer(listings, many=True)
        return Response(serializer.data)
    else:
        return Response({'listings': []})