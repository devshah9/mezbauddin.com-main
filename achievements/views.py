from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import AchievementPage


def achievement_page_view(request):
    # Assuming there is only one ServicePage or you want the first one
    context = {'page': None}
    achievement_page = AchievementPage.objects.all().first()
    if achievement_page:
        context = {
            'page': achievement_page,
        }

    return render(request, 'staging/achievements.html', context)
