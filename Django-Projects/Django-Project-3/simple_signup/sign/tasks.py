import time

from celery import shared_task

@shared_task
def test():
    print("------ TEST TASK WORKED! ------")
    return 42

@shared_task
def printer(N):
    for i in range(N):
        time.sleep(1)
        print(i+1)