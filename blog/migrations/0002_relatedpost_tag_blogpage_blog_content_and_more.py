# Generated by Django 4.2 on 2024-06-03 10:14

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RelatedPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("url", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name="blogpage",
            name="blog_content",
            field=wagtail.fields.StreamField(
                [
                    ("paragraph", wagtail.blocks.RichTextBlock()),
                    ("code", wagtail.blocks.TextBlock()),
                ],
                default="",
                use_json_field=True,
            ),
        ),
        migrations.AddField(
            model_name="blogpage",
            name="blog_meta",
            field=models.CharField(default="blog_meta", max_length=255),
        ),
        migrations.AddField(
            model_name="blogpage",
            name="blog_title",
            field=models.CharField(default="title", max_length=255),
        ),
        migrations.AddField(
            model_name="blogpage",
            name="comments",
            field=wagtail.fields.StreamField(
                [
                    (
                        "comment",
                        wagtail.blocks.StructBlock(
                            [
                                ("name", wagtail.blocks.TextBlock()),
                                ("date", wagtail.blocks.TextBlock()),
                                ("comment", wagtail.blocks.TextBlock()),
                            ]
                        ),
                    )
                ],
                blank=True,
                use_json_field=True,
            ),
        ),
        migrations.AddField(
            model_name="blogpage",
            name="header_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.CreateModel(
            name="BlogPageRelatedPosts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_posts",
                        to="blog.blogpage",
                    ),
                ),
                (
                    "related_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.relatedpost",
                    ),
                ),
            ],
        ),
    ]
