from django.db import models
import uuid
# Create your models here.


def default_board():
    return [['', '', ''], ['', '', ''], ['', '', '']]


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    board = models.JSONField(default=default_board)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    winner = models.CharField(max_length=10, default=None, null=True)


class Move(models.Model):
    game = models.ForeignKey(Game, related_name='moves',
                             on_delete=models.CASCADE)
    player = models.CharField(max_length=10)
    x = models.IntegerField()
    y = models.IntegerField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
