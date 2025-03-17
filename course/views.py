from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add


def course_home(request):
    add.delay(20, 30)
    return HttpResponse("Course Home")
