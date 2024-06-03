from django.shortcuts import render


def explore_page(request):
  return render(request, 'staging/explore.html')