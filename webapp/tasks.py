from datetime import timedelta
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from webapp.views import *

@periodic_task(run_every=timedelta(seconds=15))
def thirty_second_task():
    search(psqueue)
    search(xqueue) 
    search(pcqueue) 

