from wagtail.admin.panels import InlinePanel, FieldPanel, MultiFieldPanel
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from django.db import models
from wagtail import blocks
from wagtail.snippets.models import register_snippet

# Define the Page model
class ResumePage(Page):
    about_me = StreamField([('html', blocks.RawHTMLBlock())],blank=True, use_json_field=True)
    brand = StreamField([('html', blocks.RawHTMLBlock())],blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('about_me', classname="full"),
            FieldPanel('brand'),
        ], heading="About Me and Brand"),
        MultiFieldPanel([
            InlinePanel('personal_information', label="Personal Information"),
        ], heading="Personal Information"),
        MultiFieldPanel([
            InlinePanel('accomplishments', label="Accomplishments"),
        ], heading="Accomplishments"),
        # MultiFieldPanel([
        #     InlinePanel('education_experience', label="Education and Experience"),
        # ], heading="Education and Experience"),
        InlinePanel('education_items', label="Education"),
        InlinePanel('experience_items', label="Experience")
    ]
    



    template = "staging/about.html"



# Define the Personal Information model
class PersonalInformation(models.Model):
    page = ParentalKey(ResumePage, on_delete=models.CASCADE, related_name='personal_information')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    nationality = models.CharField(max_length=100)
    freelance_status = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    skype = models.CharField(max_length=100)
    languages = models.CharField(max_length=200)
    email = models.EmailField()

    panels = [
        FieldPanel('first_name'),
        FieldPanel('last_name'),
        FieldPanel('age'),
        FieldPanel('nationality'),
        FieldPanel('freelance_status'),
        FieldPanel('address'),
        FieldPanel('phone'),
        FieldPanel('skype'),
        FieldPanel('languages'),
        FieldPanel('email'),
    ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Personal Information"


# Define the Accomplishments model
class Accomplishments(models.Model):
    page = ParentalKey(ResumePage, on_delete=models.CASCADE, related_name='accomplishments')
    years_of_experience = models.IntegerField()
    happy_customers = models.IntegerField()
    completed_projects = models.IntegerField()
    awards_won = models.IntegerField()

    panels = [
        FieldPanel('years_of_experience'),
        FieldPanel('happy_customers'),
        FieldPanel('completed_projects'),
        FieldPanel('awards_won'),
    ]

    def __str__(self):
        return "Accomplishments"

    class Meta:
        verbose_name_plural = "Accomplishments"


class EducationItem(models.Model):
    resume_page = ParentalKey(ResumePage, on_delete=models.CASCADE, related_name='education_items')
    year = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    description = models.TextField()

    panels = [
        FieldPanel('year'),
        FieldPanel('title'),
        FieldPanel('institution'),
        FieldPanel('description'),
    ]

class ExperienceItem(models.Model):
    resume_page = ParentalKey(ResumePage, on_delete=models.CASCADE, related_name='experience_items')
    start_year = models.CharField(max_length=20)
    end_year = models.CharField(max_length=20, null=True, blank=True)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()

    panels = [
        FieldPanel('start_year'),
        FieldPanel('end_year'),
        FieldPanel('title'),
        FieldPanel('company'),
        FieldPanel('description'),
    ]