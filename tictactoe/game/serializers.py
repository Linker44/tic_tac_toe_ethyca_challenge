from rest_framework import serializers
from .models import Game, Move


class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ['player', 'x', 'y', 'date']


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'board', 'winner']
        read_only_fields = ['id', 'board', 'winner']
