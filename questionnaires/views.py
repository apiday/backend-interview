from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from questionnaires.models import Questionnaire, Question
from questionnaires.serializers import (
    QuestionnaireSerializer,
    QuestionSerializer,
)


class QuestionnaireViewSet(ListModelMixin, GenericViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class QuestionViewSet(ListModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Question.objects.all().prefetch_related("answers")
    serializer_class = QuestionSerializer
    filterset_fields = ["questionnaire"]

    def get_queryset(self):
        return super().get_queryset().filter(questionnaire__user=self.request.user)
