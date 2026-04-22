import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demonsite.settings')

app = Celery('demonsite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()