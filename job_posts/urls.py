from rest_framework import routers
from django.urls import path
from job_posts.views import JobPostViewSet

router = routers.SimpleRouter()

router.register(r'job-post', JobPostViewSet)

urlpatterns = router.urls