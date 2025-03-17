from django.urls import path

from .views import course_home, check_task_status
urlpatterns = [
        path("task/", course_home),
        path("task/<str:task_id>/", check_task_status),
]
