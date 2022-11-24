from time import sleep


def sleep_and_print(secs):
    sleep(secs)
    print("task done")
    return True

def schedule_function():
    print("calling from django_q")

    return True