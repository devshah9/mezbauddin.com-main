from django.db import models
from wagtail.fields import RichTextField, StreamField
from wagtail import blocks
from wagtail.models import Page

from wagtail.admin.panels import InlinePanel, FieldPanel, MultiFieldPanel
# Create your models here.

class ContactPage(Page):
    contact = StreamField([('html', blocks.RawHTMLBlock())],blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('achivement', classname="full"),]

    template = "staging/contacts.html"



    class Meta:
        verbose_name = "contacts Page"
        verbose_name_plural = "contacts Pages"