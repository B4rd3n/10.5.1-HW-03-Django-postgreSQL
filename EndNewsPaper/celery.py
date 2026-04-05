from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EndNewsPaper.settings')

app = Celery('EndNewsPaper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'weakly_send_mail_for_subscribers': {
        'task': 'news_portal.tasks.weakly_send',
        'schedule': crontab(hour=19, minute=58, day_of_week='sunday'),
    },
}