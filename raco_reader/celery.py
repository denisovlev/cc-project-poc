import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

app = Celery('raco_reader')
app.config_from_object('raco_reader.settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: ['raco_reader'])

app.conf.beat_schedule = {
    'Print notification titles': {
        'task': 'raco_reader.tasks.store_notifications',
        'schedule': timedelta(seconds=30),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    }
}