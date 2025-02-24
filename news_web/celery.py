import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_web.settings")


app = Celery("news_web")

app.conf.beat_schedule = {
    'print-hello-every-10-seconds': {
        'task': 'news_web_app.tasks.print_hello',
        'schedule': 10.0,  # Run every 10 seconds
    },
    'fetch-news-every-8-min': {
        'task': 'news_web_app.news.'
    }
}

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
