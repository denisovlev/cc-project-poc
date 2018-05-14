import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')

app = Celery('raco_reader')
app.config_from_object('raco_reader.settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: ['raco_reader'])

app.conf.beat_schedule = {
    'print_stuff_crontab': {
        'task': 'raco_reader.tasks.print_stuff',
        'schedule': timedelta(seconds=5),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}