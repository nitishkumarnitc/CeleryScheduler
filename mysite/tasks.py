from celery.decorators import task
from celery.utils.log import get_task_logger
from time import sleep
logger = get_task_logger(__name__)
# from celery.task.schedules import crontab
# from celery.decorators import periodic_task

@task(name='my_first_task')
def my_first_task(duration):
    sleep(duration)
    return('first_task_done')

@task(name='create_task')
def create_task(payload):
    return('create_task_done')


@task(name='cancel_task')
def cancel_task(task_id):
    return('cancelled _task_id '+task_id)

# @periodic_task(run_every=(crontab(minute='*/15')), name="task_save_latest_flickr_image", ignore_result=True)
# def task_save_latest_flickr_image():
#     """
#     Saves latest image from Flickr
#     """
#     logger.info("Saved image from Flickr")

#normal function call in python
my_first_task(10)
#add task to the celery with function call
my_first_task.delay(10)
