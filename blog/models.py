from django.db import models
from django import forms
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import RichTextBlock, TextBlock, StructBlock
from wagtail.search import index
from wagtail.images.models import Image
from wagtail.images.widgets import AdminImageChooser

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        context = super().get_context(request)
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag) if tag else BlogPage.objects.all()
        context['blogpages'] = blogpages
        return context

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog categories'

class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    header_image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    blog_title = models.CharField(max_length=255, default="title")
    blog_meta = models.CharField(max_length=255, default="blog_meta")
    blog_content = StreamField([
        ('paragraph', RichTextBlock()),
        ('code', TextBlock()),
    ], use_json_field=True, default="")
    comments = StreamField([
        ('comment', StructBlock([
            ('name', TextBlock()),
            ('date', TextBlock()),
            ('comment', TextBlock()),
        ])),
    ], use_json_field=True, blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    @staticmethod
    def get_recent_posts():
        return BlogPage.objects.live().order_by('-first_published_at')[:5]

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('header_image', widget=AdminImageChooser),
        FieldPanel('blog_title'),
        FieldPanel('blog_meta'),
        FieldPanel('blog_content'),  # Use FieldPanel for StreamField
        FieldPanel('comments'),  # Use FieldPanel for StreamField
        InlinePanel('gallery_images', label="Gallery images"),
        InlinePanel('related_posts', label="Related posts"),
    ]

    template = "staging/blog-content.html"

class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

@register_snippet
class RelatedPost(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel('title'),
        FieldPanel('url'),
    ]

    def __str__(self):
        return self.title

class BlogPageRelatedPosts(models.Model):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='related_posts')
    related_post = models.ForeignKey(RelatedPost, on_delete=models.CASCADE)

    panels = [
        FieldPanel('related_post'),
    ]

@register_snippet
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# class BlogPageTag(models.Model):
#     page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='blog_page_tags', null=True)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

#     panels = [
#         FieldPanel('tag'),
#     ]
