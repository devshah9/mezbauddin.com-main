from django.shortcuts import render
from .models import BlogPage
from wagtail.models import Page
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

def blog_index_page(request):
    blogpages = BlogPage.objects.live().order_by('-date')
    context = {'blogpages': blogpages}
    return render(request, 'staging/blog-main.html', context)

class BlogDetailView(RoutablePageMixin, Page):
    template = "staging/blog-content.html"

    @route(r'^$', name='blog_detail')
    def blog_detail(self, request):
        context = self.get_context(request)
        context['blogpage'] = BlogPage.objects.get(slug=self.slug)
        return render(request, self.template, context)
