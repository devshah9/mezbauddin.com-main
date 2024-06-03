from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import ResumePage

def resume_page_view(request):
    # Assuming there is only one ServicePage or you want the first one
    context = {'page': None}
    resume_page = ResumePage.objects.all().first()
    if resume_page:
        context = {
            'page': resume_page,
        }

    return render(request, 'staging/about.html', context)