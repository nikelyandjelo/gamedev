from unittest import TestCase
from unittest.mock import patch
from yahtzee import process_winner
import io


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_process_winner_player1_won(self, mock_sdtout):
        process_winner(100, 0)
        expected = 'USER 1 won by 100 points! Congratulations!\n'
        self.assertEqual(expected, mock_sdtout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_process_tie(self, mock_sdtout):
        process_winner(100, 100)
        expected = "Wow! After such long game both players scored the same amount of points! That's very rare!\n"
        self.assertEqual(expected, mock_sdtout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_process_player2_won(self, mock_sdtout):
        process_winner(0, 100)
        expected = 'USER 2 won by 100 points! Congratulations!\n'
        self.assertEqual(expected, mock_sdtout.getvalue())


