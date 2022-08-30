import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')
# ^ Setted module and string path to settings

app = Celery('Workers')
app.config_from_object('django.conf:settings', namespace='CELERY')
# ^ Name space will be first name arg from module path in setting

app.autodiscover_tasks()
