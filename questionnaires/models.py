from django.contrib.auth.models import User
from django.db import models


class Questionnaire(models.Model):
    class Status(models.TextChoices):
        UNANSWERED = "UNANSWERED"
        ANSWERING = "ANSWERING"
        COMPLETE = "COMPLETE"

    name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=10, choices=Status.choices, blank=True, default=Status.UNANSWERED
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Question(models.Model):
    class Status(models.TextChoices):
        UNANSWERED = "UNANSWERED"
        ANSWERED_BY_CUSTOMER = "ANSWERED"

    class Type(models.TextChoices):
        FREE_TEXT = "FREE_TEXT"
        SINGLE_SELECT = "SINGLE_SELECT"
        MULTIPLE_SELECT = "MULTIPLE_SELECT"

    index = models.IntegerField()
    hint = models.TextField(blank=True)
    type = models.CharField(max_length=25, choices=Type.choices)
    status = models.CharField(
        max_length=16, choices=Status.choices, blank=True, default=Status.UNANSWERED
    )
    questionnaire = models.ForeignKey(
        Questionnaire, on_delete=models.CASCADE, related_name="questions"
    )
    text = models.TextField()


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    index = models.IntegerField()
    text = models.TextField(
        blank=True, default="", help_text="Text displayed for select questions"
    )
    user_text = models.TextField(
        blank=True,
        default="",
        help_text="Text written by the user for FREE_TEXT questions",
    )
    selected = models.BooleanField(default=False)
