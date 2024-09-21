from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction

from questionnaires.models import Questionnaire, Question, Answer


class Command(BaseCommand):
    help = "Create some questionnaires in the database if none exists."

    @transaction.atomic
    def handle(self, *args, **options):
        if Questionnaire.objects.count() > 0:
            print("Questionnaire already exists. Nothing will be created.")
            return
        if User.objects.count() == 0:
            print(
                'A user should be created before creating questionnaires. Please run "python manage.py createsuperuser"'
            )
            return
        user = User.objects.first()
        questionnaire = Questionnaire.objects.create(name="ESG campaign", user=user)
        question_1 = Question.objects.create(
            index=1,
            type=Question.Type.FREE_TEXT,
            questionnaire=questionnaire,
            text="What is the weather like today?",
        )
        Answer.objects.create(question=question_1, index=1)
        question_2 = Question.objects.create(
            index=2,
            type=Question.Type.SINGLE_SELECT,
            questionnaire=questionnaire,
            text="Do you have a hat?",
        )
        Answer.objects.create(question=question_2, index=1, text="Yes")
        Answer.objects.create(question=question_2, index=2, text="No")
        question_3 = Question.objects.create(
            index=3,
            type=Question.Type.MULTIPLE_SELECT,
            questionnaire=questionnaire,
            text="Which fruits do you like?",
        )
        Answer.objects.create(question=question_3, index=1, text="Apple")
        Answer.objects.create(question=question_3, index=2, text="Orange")
        Answer.objects.create(question=question_3, index=3, text="Mango")
        Answer.objects.create(question=question_3, index=4, text="Pear")
        Answer.objects.create(question=question_3, index=5, text="None of the above")
