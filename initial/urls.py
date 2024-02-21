from django.urls import path
from .views import home, men, women, baby

urlpatterns = [
    path('', home),
    path('categories/', men),
    path('categories/', women),
    path('categories/', baby),
]