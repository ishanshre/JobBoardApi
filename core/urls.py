from rest_framework.routers import DefaultRouter

from rest_framework_nested import routers

from core import views

router = DefaultRouter()

router.register("jobs", views.JobModelViewSet, basename="jobs")
job_router = routers.NestedDefaultRouter(router, 'jobs', lookup="job")
job_router.register("jobs-apply", views.JobApplyModelViewSet, basename='job-applies')
urlpatterns = router.urls + job_router.urls