from django.shortcuts import render
import json
from django.http import JsonResponse
from django_q.tasks import async_task, result_group, schedule
from django_q.models import Schedule
import arrow


# Create your views here.
def django_q_test(request):
    print(request)
    json_payload = {"message": "hello world!"}
    # async_task('math.copysign', 2, -2)
    for i in range(10):
        async_task("django_q_tasks_app.services.sleep_and_print", 20, hook='django_q_tasks_app.hooks.print_result')
    return JsonResponse(json_payload)


# for group wise queue

def django_q_group(request):
    for i in range(4):
        async_task('math.modf', i, group='modf')

    # wait until the group has 4 results
    result = result_group('modf', count=4)
    print(result)




    """ for iterable 


    # set up a list of arguments for math.floor
    iter = [i for i in range(100)]

    # async_task iter them
    id=async_iter('math.floor',iter)

    # wait for the collated result for 1 second
    result_list = result(id, wait=1000)

    """

def schedule_tsk(request):
    json_payload = {'result': 'hellow boys whats up'}
    schedule('django_q_tasks_app.services.schedule_function',
         schedule_type=Schedule.MINUTES,
         minutes=1,
         repeats=24)
        #  next_run=arrow.utcnow().replace(hour=18, minute=0))

    return JsonResponse(json_payload)
