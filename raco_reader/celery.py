import os
from datetime import timedelta
from django.conf import settings
from celery import Celery

app = Celery('raco_reader')
app.config_from_object('django.conf:settings', namespace='CELERY')
RACO_READER_INTERVAL = getattr(settings, "RACO_READER_INTERVAL", 3600)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: ['raco_reader'])

app.conf.beat_schedule = {
    'Store notifications': {
        'task': 'raco_reader.tasks.store_notifications',
        'schedule': timedelta(seconds=RACO_READER_INTERVAL),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    }
}