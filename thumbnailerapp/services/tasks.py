from celery import Celery
from thumbnailerapp.services.main import thumbnail

celeryapp = Celery('tasks', broker='pyamqp://guest@localhost:5672//')

@celeryapp.task
def thumbnail_task(input_filename, output_filename, width, height):
    return thumbnail(input_filename, output_filename, width, height)