from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import CharBlock, RichTextBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks

class ServiceBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    title = CharBlock(required=True)
    description = RichTextBlock(required=True)

    class Meta:
        icon = "placeholder"
        label = "Service"

class ServiceTitleBlock(StructBlock):
    title = CharBlock(required=True)

    class Meta:
        icon = "title"
        label = "Service Title"

class ApplicationBlock(StructBlock):
    title = CharBlock(required=True)
    description = RichTextBlock(required=True)

    class Meta:
        icon = "doc-full"
        label = "Application"

class ServicePage(Page):

    first_part = StreamField([('html', blocks.RawHTMLBlock())],blank=True, use_json_field=True)
    second_part = StreamField([('html', blocks.RawHTMLBlock())],blank=True, use_json_field=True)
    third_part = StreamField([('html', blocks.RawHTMLBlock())],blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('first_part'),
        FieldPanel('second_part'),
        FieldPanel('third_part'),
    ]

    template = "staging/services.html"

    class Meta:
        verbose_name = "Service Page"
        verbose_name_plural = "Service Pages"

