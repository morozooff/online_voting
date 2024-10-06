from django.db import models
from datetime import datetime

class Poll(models.Model):
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now)

class  Choice(models.Model):
    text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    poll_id = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    