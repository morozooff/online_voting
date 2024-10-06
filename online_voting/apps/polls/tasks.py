from celery import shared_task
from .db_repo import update_choice

from time import sleep

@shared_task
def process_vote(choice_id: int):
    sleep(2)
    print("your choice is rendering...")
    sleep(2)
    print("...")
    return update_choice(choice_id)
