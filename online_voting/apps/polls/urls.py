from django.urls import path
from .views import PollListView, PollDetailView, VoteView

urlpatterns = [
    path('polls/', PollListView.as_view(), name='poll-list'),
    path('polls/<int:pk>/', PollDetailView.as_view(), name='poll-detail'),
    path('choices/<int:pk>/vote/', VoteView.as_view(), name='vote'),
]