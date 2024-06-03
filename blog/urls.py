from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index_page, name='index'),  # URL pattern for the main blog page
    # Add more URL patterns as needed for other blog pages
    path('<slug:slug>', views.blog_index_page, name='blog_detail')
]
