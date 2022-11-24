from django.apps import AppConfig

class DjangoQTasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_q_tasks_app'

    def ready(self):
        pass

        # from django_q.tasks import async_task, result

        # # create the task
        # # async_task('math.copysign', 2, -2)

        # # or with import and storing the id
        # from math import copysign

        # task_id = async_task(copysign, 2, -2)
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> tsk_id", task_id)

        # # get the result
        # # task_result = result(task_id)
        

        # # result returns None if the task has not been executed yet
        # # you can wait for it
        # task_result = result(task_id, 200)
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", task_result)

        # # but in most cases you will want to use a hook:

        # # async_task('math.modf', 2.5, hook='hooks.print_result')

        # opts = {'hook': 'hooks.print_result',
        #             'group': 'math',
        #             'timeout': 30}

        # async_task('math.modf', 2.5, q_options=opts)

        # # # hooks.py
        # # def print_result(task):
        # #     print(task.result)
        
