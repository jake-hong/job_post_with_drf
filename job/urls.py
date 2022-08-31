from django.urls import path, include

urlpatterns = [
    path("api/", include('job_posts.urls'))
]
