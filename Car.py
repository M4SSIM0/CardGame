class Car:
    def __init__(self, id: int, name: str, hp: int, weight: int, length: int,
                 kw: int, topspeed: int, acceleration: int, price: int):
        self.id = id
        self.name = name
        self.hp = hp
        self.weight = weight
        self.length = length
        self.kw = kw
        self.topspeed = topspeed
        self.acceleration = acceleration
        self.price = price

    def __str__(self):
        return f"{self.name} has {self.hp} HP, {self.weight} kg, {self.length} cm, " \
               f"{self.kw} Kw, {self.topspeed} km/h, {self.acceleration} s, {self.price} $"


