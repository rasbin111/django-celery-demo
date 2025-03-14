import os

from celery import Celery
from django.conf import settings

app = Celery("django-celery-demo")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-celery-demo.settings')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


