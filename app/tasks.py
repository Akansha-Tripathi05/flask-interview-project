from celery import Celery
from .config import Config


celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)
celery.conf.result_backend = Config.CELERY_RESULT_BACKEND


@celery.task
def add(x, y):
    return x + y