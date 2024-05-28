from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL pattern for the main blog page
    # Add more URL patterns as needed for other blog pages
]
