from django.shortcuts import render
from django.http import HttpResponse
from celery.result import AsyncResult
from .tasks import add


def course_home(request):
    result = add.delay(20, 30)

    return HttpResponse(f"Task ID: {result.id}")


def check_task_status(request, task_id):
    result = AsyncResult(task_id)

    if result.ready():
        return HttpResponse(f"Task Result: {result.result}")
    else:
        return HttpResponse(f"Task is still running")