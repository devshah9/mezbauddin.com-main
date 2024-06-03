# Generated by Django 4.2 on 2024-06-03 10:14

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
    ]

    operations = [
        migrations.CreateModel(
            name="AchievementPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "achivement",
                    wagtail.fields.StreamField(
                        [("html", wagtail.blocks.RawHTMLBlock())],
                        blank=True,
                        use_json_field=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Achievement Page",
                "verbose_name_plural": "Achievement Pages",
            },
            bases=("wagtailcore.page",),
        ),
    ]