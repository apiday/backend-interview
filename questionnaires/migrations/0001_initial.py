# Generated by Django 5.1.1 on 2024-09-19 20:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Question",
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
                ("index", models.IntegerField()),
                ("hint", models.TextField(blank=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("FREE_TEXT", "Free Text"),
                            ("SINGLE_SELECT", "Single Select"),
                            ("MULTIPLE_SELECT", "Multiple Select"),
                        ],
                        max_length=25,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("UNANSWERED", "Unanswered"),
                            ("ANSWERED", "Answered By Customer"),
                        ],
                        default="UNANSWERED",
                        max_length=16,
                    ),
                ),
                ("text", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Answer",
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
                ("index", models.IntegerField()),
                (
                    "text",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="Text displayed for select questions",
                    ),
                ),
                (
                    "user_text",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="Text written by the user for FREE_TEXT questions",
                    ),
                ),
                ("selected", models.BooleanField(default=False)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        to="questionnaires.question",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Questionnaire",
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
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("UNANSWERED", "Unanswered"),
                            ("ANSWERING", "Answering"),
                            ("COMPLETE", "Complete"),
                        ],
                        default="UNANSWERED",
                        max_length=10,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="question",
            name="questionnaire",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="questionnaires.questionnaire",
            ),
        ),
    ]
