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




