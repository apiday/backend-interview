from django.dispatch import receiver
from django.db.models.signals import post_save

from questionnaires.models import Answer, Question, Questionnaire


@receiver(post_save, sender=Answer)
def update_question_status(sender, **kwargs):
    answer: Answer = kwargs["instance"]
    if (
        answer.selected
        and answer.question.status != Question.Status.ANSWERED_BY_CUSTOMER
    ):
        answer.question.status = Question.Status.ANSWERED_BY_CUSTOMER
        answer.question.save()

@receiver(post_save, sender=Question)
def update_questionnaire_status(sender, **kwargs):
    question: Question = kwargs["instance"]
    if (
        question.status == Question.Status.ANSWERED_BY_CUSTOMER
        and question.questionnaire.status == Questionnaire.Status.UNANSWERED
    ):
        question.questionnaire.status = Questionnaire.Status.ANSWERING
        question.questionnaire.save()
