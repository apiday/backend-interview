from rest_framework.routers import DefaultRouter

from questionnaires.views import QuestionViewSet, QuestionnaireViewSet

router = DefaultRouter()
router.register(r"questions", QuestionViewSet, basename="questions")
router.register(r"questionnaires", QuestionnaireViewSet, basename="questionnaires")
urlpatterns = router.urls
