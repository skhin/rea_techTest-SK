from django.urls import path, include
from listings import views

urlpatterns = [
    path('latest-listings/', views.LatestListingsList.as_view()),
    path('listings/<slug:country_slug>/<slug:listings_slug>/', views.ListingsDetail.as_view()),
    
]