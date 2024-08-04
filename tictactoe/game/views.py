from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Game, Move
from .serializers import GameSerializer, MoveSerializer
from .helpers import is_move_valid, make_move, check_winner


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('-date')
    serializer_class = GameSerializer

    @action(detail=True, methods=['put', 'patch'])
    def move(self, request, pk=None):
        game = Game.objects.get(pk=pk)
        x = request.data.get('x')
        y = request.data.get('y')

        if not is_move_valid(game.board, x, y, game.winner):
            return Response({'error': 'Invalid Move'}, status=status.HTTP_400_BAD_REQUEST)

        game.board[x][y] = 'X'

        Move.objects.create(game=game, x=x, y=y, player='user')

        game.winner = 'X' if check_winner(game.board, 'X') else None

        bot_move = make_move(game.board)

        if bot_move is None and game.winner is None:
            game.winner = 'Draw'

        if bot_move and game.winner is None:
            ax, ay = bot_move
            game.board[ax][ay] = 'O'
            Move.objects.create(game=game, x=ax, y=ay, player='bot')
            game.winner = 'O' if check_winner(game.board, 'O') else None

        game.save()
        serializer = GameSerializer(game)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def list_moves(self, request, pk=None):
        game = Game.objects.get(pk=pk)
        moves = Move.objects.filter(game=game).order_by('date')
        serializer = MoveSerializer(moves, many=True)
        return Response(serializer.data)
