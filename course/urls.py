from django.urls import path

from .views import course_home
urlpatterns = [
        path("course/", course_home)
        ]
