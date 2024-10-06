from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .db_repo import *
from .tasks import process_vote

class PollListView(APIView):
    def get(self, request: Request) -> Response:
        polls_list = get_all_polls()
        print(polls_list)
        result = [poll.to_json for poll in polls_list.polls]

        return Response(result, status=status.HTTP_200_OK)


class PollDetailView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        try:
            poll = get_poll(pk)
            choices_list = get_all_choices_for_poll(poll.id)

            result = poll.to_json
            result["choices"] = [choice.to_json for choice in choices_list.choices]
            return Response(result, status=status.HTTP_200_OK)
        except ValueError:
            return Response({"error": "Poll not found"}, status=status.HTTP_404_NOT_FOUND)


class VoteView(APIView):
    def post(self, request: Request, pk: int) -> Response:
        try:
            process_vote.delay(pk)
            return Response({"message": "Vote counted!"}, status=status.HTTP_200_OK)
        except ValueError:
            return Response({"error": "Choice not found"}, status=status.HTTP_404_NOT_FOUND)