from django.urls import path
from django_q_tasks_app import views

app_name = 'django_q'

urlpatterns = [
    path('test/', views.django_q_test, name='django_q test' ),
    path('schedule/', views.schedule_tsk, name=' schedule function')
]