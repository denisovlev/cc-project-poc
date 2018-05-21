from datetime import timedelta
from django.conf import settings
from celery import Celery

app = Celery('mailer_job')
app.config_from_object('django.conf:settings', namespace='CELERY')
MAILER_JOB_INTERVAL = getattr(settings, "MAILER_JOB_INTERVAL", 3600)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: ['mailer_job'])

app.conf.beat_schedule = {
    'Send emails': {
        'task': 'mailer_job.tasks.send_emails',
        'schedule': timedelta(seconds=MAILER_JOB_INTERVAL),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    }
}