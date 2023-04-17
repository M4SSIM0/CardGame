import random

from Car import Car
from Deck import Deck


class Player:
    def __init__(self, name: str, id: int):
        self.name = name
        self.deck = Deck(id)
        self.current_card = None  # Initialize the current_card attribute to None

    def __str__(self):
        return self.name

    def get_new_deck(self):
        """
        Get a new deck.
        :return:
        """
        self.deck = Deck()
        self.current_card = None  # Reset the current_card attribute to None

    def draw_card(self):
        """
        Draw a random card from the deck.
        :return:
        """
        self.current_card = random.choice(self.deck.cards)  # Set the current_card attribute to a random card
        # self.deck.cards.remove(self.current_card)  # Remove the current_card from the deck
        return self.current_card

    def check_card(self, card: Car):
        """
        Check if the card is in the deck.
        :param card: card to check
        :return: bool - True if the card is in the deck, False otherwise
        """
        for i in self.deck.cards:
            if i.id == card.id:
                return True
        return False

    def add_card(self, card: Car):
        """
        Add a card to the deck.
        :param card: card to add
        :return:
        """
        self.deck.cards.append(card)
        self.deck.card_count += 1
        print(f"--{self.name} HAS {self.deck.card_count} CAR(D)S.--")

    def remove_card(self, card: Car):
        """
        Remove a card from the deck.
        :param card:
        :return:
        """
        self.deck.cards.remove(card)
        self.deck.card_count -= 1
        print(f"->{self.name} HAS {self.deck.card_count} CAR(D)S.<-")

    @staticmethod
    def choose_topic():
        """
        Choose a topic to compare the cards.
        :return:
        """
        topics = ['hp', "weight", "length", "kw", "topspeed", "acceleration", "price"]
        print('║║ CHOOSE A TOPIC: ')
        for i, topic in enumerate(topics):
            print(f"║║ {i + 1}. {topic} ")
        while True:
            choice = int(input()) - 1
            if 0 <= choice < len(topics):
                break
            print('║║ Invalid choice, try again ')
        return topics[choice]

    def compare(self, other, attribute: str):
        """
        Compare the current cards of the players.
        :param other:
        :param attribute:
        :return:
        """
        match attribute.lower():
            case "hp":
                if self.current_card.hp < other.current_card.hp:
                    return self
                elif self.current_card.hp > other.current_card.hp:
                    return other
                else:
                    return type('obj', (Player,), {'name': 'tie', 'deck': None, 'current_card': None})
            case "weight":
                if self.current_card.weight < other.current_card.weight:
                    return other
                elif self.current_card.weight > other.current_card.weight:
                    return self
                else:
                    return type('obj', (Player,), {'name': 'tie', 'deck': None, 'current_card': None})
            case "length":
                if self.current_card.length < other.current_card.length:
                    return other
                elif self.current_card.length > other.current_card.length:
                    return self
                else:
                    return type('obj', (Player,), {'name': 'tie', 'deck': None, 'current_card': None})
            case "kw":
                if self.current_card.kw < other.current_card.kw:
                    return self
                elif self.current_card.kw > other.current_card.kw:
                    return other
                else:
                    return type('obj', (Player,), {'name': 'tie', 'deck': None, 'current_card': None})
            case "topspeed":
                if self.current_card.topspeed < other.current_card.topspeed:
                    return self
                elif self.current_card.topspeed > other.current_card.topspeed:
                    return other
                else:
                    return type('obj', (Player,), {'name': 'tie', 'deck': None, 'current_card': None})
            case "acceleration":
                if self.current_card.acceleration < other.current_card.acceleration:
                    return other
                elif self.current_card.acceleration > other.current_card.acceleration:
                    return self
                else:
                    return type('obj', (Player,), {'name': 'tie', 'deck': None, 'current_card': None})
            case "price":
                if self.current_card.price < other.current_card.price:
                    return self
                elif self.current_card.price > other.current_card.price:
                    return other
                else:
                    return type('obj', (Player,), {'name': 'tie', 'deck': None, 'current_card': None})
