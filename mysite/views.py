from django.http import HttpResponse
from .tasks import my_first_task
from .tasks import create_task
from .tasks import cancel_task
def index(request):
    my_first_task.delay(10)
    return HttpResponse('response done')

def create_task(request) :
    create_task(request)
    return HttpResponse('Task Created')
def cancel_task(request):
    cancel_task(request)
    return HttpResponse('Task Cancelled')
def get_all_task(request):
    return  HttpResponse("All Tasks")
def get_task(request):
    return  HttpResponse("Task")
