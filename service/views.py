from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import ServicePage

def service_page_view(request):
    # Assuming there is only one ServicePage or you want the first one
    context = {
        'page': None,
    }
    service_page = ServicePage.objects.all().first()
    if service_page:
        context = {
            'page': service_page,
        }
    return render(request, 'staging/services.html', context)