import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'raco_reader.settings')

app = Celery('raco_reader')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()