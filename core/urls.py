from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()

router.register("jobs", views.JobModelViewSet, basename="jobs")

urlpatterns = router.urls