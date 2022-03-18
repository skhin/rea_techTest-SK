from django.urls import path, include
from listings import views

urlpatterns = [
    path('latest-listings/', views.LatestListingsList.as_view()),
    
]