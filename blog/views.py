from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     # Logic for handling the blog page request
#     # For example, fetching blog posts from a database
#     # and passing them to a template for rendering
#     context = {
#         'blog_posts': [
#             {'title': 'First Blog Post', 'content': 'Lorem ipsum dolor sit amet...'},
#             {'title': 'Second Blog Post', 'content': 'Consectetur adipiscing elit...'},
#             # Add more blog posts as needed
#         ]
#     }
#     return render(request, 'blog/blog_index_page.html', context)
from django.shortcuts import render
from .models import BlogPage

def blog_index_page(request):
  blogpages = BlogPage.objects.live().order_by('-date')
  context = {'blogpages': blogpages}
  return render(request, 'staging/blog-main.html', context)

def blog_page(request, slug):
  blogpages = BlogPage.objects.get(slug=slug)
  context = {'blogpages': blogpages}
  return render(request, 'staging/blog-content.html', context)


