from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Game, Move


class GameTests(APITestCase):

    def test_create_game(self):
        url = reverse('game-list')
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertEqual(len(response.data['board']), 3)

    def test_list_games(self):
        url = reverse('game-list')
        game_1 = Game.objects.create()
        game_2 = Game.objects.create()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        # test that the games are listed chronologically
        self.assertEqual(response.data[0]['id'], str(game_1.id))
        self.assertEqual(response.data[1]['id'], str(game_2.id))

    def test_get_game(self):
        game = Game.objects.create()
        url = reverse('game-detail', args=[game.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('id', response.data)
        self.assertEqual(response.data['id'], str(game.id))

    def test_put_valid_move(self):
        game = Game.objects.create()
        url = reverse('game-move', args=[game.id])
        data = {'x': 0, 'y': 0}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # we test that the player was made
        self.assertEqual(response.data['board'][0][0], 'X')
        # we test that the computer move was made
        self.assertTrue(
            any(response.data['board'][i][j] == 'O' for i in range(3) for j in range(3)))

    def test_put_invalid_move(self):
        game = Game.objects.create()
        url = reverse('game-move', args=[game.id])
        data = {'x': 5, 'y': 0}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
        self.assertIn(response.data['error'], 'Invalid Move')

    def test_list_moves(self):
        game = Game.objects.create()
        Move.objects.create(x=0, y=0, player='user', game=game)
        Move.objects.create(x=1, y=2, player='bot', game=game)
        url = reverse('game-list-moves', args=[game.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        # test that the moves are listed chronologically
        self.assertEqual(response.data[0]['x'], 0)
        self.assertEqual(response.data[0]['y'], 0)
        self.assertEqual(response.data[1]['x'], 1)
        self.assertEqual(response.data[1]['y'], 2)

    def test_delete_game(self):
        game_1 = Game.objects.create()
        url = reverse('game-detail', args=[game_1.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Game.objects.count(), 0)
