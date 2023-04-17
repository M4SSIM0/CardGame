from Player import Player


class Game:
    def __init__(self, player, bot):
        self.player = player
        self.bot = bot
        self.player_turn = True
        self.current_card = None

    def start(self):
        while True:
            if self.player_turn:
                print(f"->YOUR TURN, {self.player.name}.")
                self.player_turn = False
            else:
                print(f"--BOT's TURN, {self.bot.name}.")
                self.player_turn = True
            topic = Player.choose_topic()
            print('->CHOOSEN TOPIC<-: ', topic)

            print('...DRAWING CARDS...')
            self.player.draw_card()
            self.bot.draw_card()

            print(f'DRAWN CARD FROM {self.player.name}: ', self.player.current_card)
            print('DRAWN CARD FROM BOT: ', self.bot.current_card)
            losing_player = self.player.compare(self.bot, topic)

            match losing_player.name:
                case self.player.name:
                    print('BOT WON THE ROUND.')
                    self.bot.add_card(losing_player.current_card)
                    self.player.remove_card(losing_player.current_card)
                    if self.player.deck.card_count == 0:
                        print("BOT HAS WON! ( ͡❛ ‿‿ ͡❛)")
                        break
                case self.bot.name:
                    print(f'{self.player.name} WON THE ROUND.')
                    self.player.add_card(losing_player.current_card)
                    self.bot.remove_card(losing_player.current_card)
                    if self.bot.deck.card_count == 0:
                        print(f"{self.player.name} HAS WON! ( ͡~ ‿‿ ͡°)")
                        break
                case default:
                    print('TIE. ¯\_( ͡~ ‿‿ ͡°)_/¯')

            if self.player_turn:
                self.player_turn = False
            else:
                self.player_turn = True


# press a button to start the game
game = Game(Player(input(
    """
██     ██ ███████ ██       ██████  ██████  ███    ███ ███████     ████████  ██████      ██     ██  █████  ██████       ██████  ███████      ██████  █████  ██████   ██ ██████  ██  ███████     
██     ██ ██      ██      ██      ██    ██ ████  ████ ██             ██    ██    ██     ██     ██ ██   ██ ██   ██     ██    ██ ██          ██      ██   ██ ██   ██ ██  ██   ██  ██ ██          
██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████          ██    ██    ██     ██  █  ██ ███████ ██████      ██    ██ █████       ██      ███████ ██████  ██  ██   ██  ██ ███████     
██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██             ██    ██    ██     ██ ███ ██ ██   ██ ██   ██     ██    ██ ██          ██      ██   ██ ██   ██ ██  ██   ██  ██      ██     
 ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████        ██     ██████       ███ ███  ██   ██ ██   ██      ██████  ██           ██████ ██   ██ ██   ██  ██ ██████  ██  ███████ 
 
 
                                                                            ║║ TO START THE GAME, ENTER YOUR NAME║║
                                                                            ║║                                   ║║
                                                                                            """),
    1), Player('Bot', 2))
game.start()
