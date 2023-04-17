import json
import random

from Car import Car

possible_cards = json.load(open("cars.json"))


class Deck:
    def __init__(self, id: int):
        self.name = f"{id}"
        self.id = id
        self.cards = []
        self.card_count = 6  # überarbeiten?
        self._create_deck()

    def _create_deck(self):
        """
        Create a Deck of 6 cars for each player.
        :return:
        """
        for i in range(6):
            card = random.choice(possible_cards)
            for x in possible_cards:
                if x["id"] == card["id"]:
                    possible_cards.remove(x)
            car = Car(id=card["id"], name=card["name"], hp=card["hp"], weight=card["weight"], length=card["length"],
                      kw=card["kw"], topspeed=card["topspeed"], acceleration=card["acceleration"], price=card["price"])
            self.cards.append(car)

        print(f"║║ DECK {self.name} ║║")
        for c in self.cards:
            print(f"-{c}")

    def shuffle(self):
        """
        Shuffle the deck of cards.
        :return:
        """
        random.shuffle(self.cards)

    def is_empty(self):
        """
        Check if the deck is empty.
        :return:
        """
        return True if len(self.cards) == 0 else False
