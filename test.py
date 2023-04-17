import unittest

from Player import Player


class Test(unittest.TestCase):
    def test_automatic_game(self):
        player1 = Player("Player1", 1)
        player2 = Player("Player2", 2)

        x = 0

        while True:
            x += 1
            print('round', x)
            # Ziehe karten
            c1 = player1.draw_card()
            print('Card from player 1:', c1)
            # print('ID from card player 1:', id(c1))
            c2 = player2.draw_card()
            print('Card from player 2:', c2)
            # print('ID from card player 2:', id(c2))

            # Vergleiche karten
            loser_card = c1.compare(c2, "price")
            print('Loser card:', loser_card)
            # print('ID from loser card:', id(loser_card))

            if player1.check_card(loser_card):
                print('remove from player 1')
                player1.remove_card(loser_card)
                player2.add_card(loser_card)
            elif player2.check_card(loser_card):
                print('remove from player 2')
                player2.remove_card(loser_card)
                player1.add_card(loser_card)

            # Prüfen, ob ein Spieler keine Karten mehr hat
            if player1.deck.is_empty():
                print("Player2 hat gewonnen!")
                break
            elif player2.deck.is_empty():
                print("Player1 hat gewonnen!")
                break

    def test_real_game(self):
        player1 = Player(input('Name of player 1: '), 1)
        player2 = Player(input('Name of player 2: '), 2)

        current_player = player1

        while True:
            print(f'Turn of player {current_player}.')
            topic = Player.choose_topic()
            print('chosen topic:', topic)

            print('Drawing cards...')
            player1.draw_card()
            player2.draw_card()

            print('drawn card from player 1:', player1.current_card)
            print('drawn card from player 2:', player2.current_card)
            losing_player = player1.compare(player2, topic)

            match losing_player.name:
                case player1.name:
                    print('Player 2 won the round.')
                    player2.add_card(losing_player.current_card)
                    player1.remove_card(losing_player.current_card)
                    if player1.deck.card_count == 0:
                        print("Player2 has won!")
                        break
                case player2.name:
                    print('Player 1 won the round.')
                    player1.add_card(losing_player.current_card)
                    player2.remove_card(losing_player.current_card)
                    if player2.deck.card_count == 0:
                        print("Player1 has won!")
                        break
                case default:
                    print('Tie.')

            if current_player == player1:
                current_player = player2
            else:
                current_player = player1
