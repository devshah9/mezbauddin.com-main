from django.shortcuts import render

def staging_home(request):
    return render(request, 'staging/home.html')
def menu_page(request):
    return render(request, 'staging/menu.html')
def about_page(request):
    return render(request, 'staging/about.html')
def achievements_page(request):
    return render(request, 'staging/achievements.html')
def blog_page(request):
    return render(request, 'staging/blog.html')
def contact_page(request):
    return render(request, 'staging/contact.html')
def services_page(request):
    return render(request, 'staging/services.html')
def explore(request):
    return render(request, 'staging/explore.html')