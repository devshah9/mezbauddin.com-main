from django.urls import path
from . import views
from .views import menu_page  # Make sure this import is correct
from .views import about_page  # Make sure this import is correct
app_name = 'staging'

urlpatterns = [
    path('', views.staging_home, name='home'),
    path('explore/',views.explore,name='explore'),
    path('about/', views.about_page, name='about_page'),
    path('services/', views.services_page, name='services_page'),
    path('achievements/', views.achievements_page, name='achievements_page'),
    path('blog/', views.blog_page, name='blog_page'),
    path('contact/', views.contact_page, name='contact_page'),
    # ... other staging URLs ...
]