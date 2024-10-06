from django.shortcuts import get_object_or_404

from .objects import Poll, PollList, Choice, PollChoices
from .models import Poll as DBPoll, Choice as DBChoice

def get_all_polls() -> PollList:
    queryset = DBPoll.objects.all()

    polls = []
    for item in queryset:
        current_poll = Poll(
            id = item.pk,
            question = item.question,
            created_at=item.created_at,
            )
        polls.append(current_poll)
        
    return PollList(polls=polls)

def get_poll(poll_id: int) -> Poll:
    item = get_object_or_404(DBPoll, pk=poll_id)
    
    return Poll(
            id = item.pk,
            question = item.question,
            created_at=item.created_at,
            )

def get_all_choices_for_poll(poll_id: int):
    queryset = DBChoice.objects.filter(poll_id=poll_id)

    choice_list = []
    for item in queryset:
        current_choice = Choice(
            id = item.pk,
            text=item.text,
            votes=item.votes,
        )
        choice_list.append(current_choice)
    
    return PollChoices(choices=choice_list)

def update_choice(choice_id: int) -> str:
    choice = get_object_or_404(DBChoice, pk=choice_id)
    choice.votes += 1
    choice.save()

    return choice.text
