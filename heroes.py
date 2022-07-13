from abc import ABC, abstractmethod


class Gun:

    @staticmethod
    def fire_a_gun():
        print("PIU PIU")


class Laser:

    @staticmethod
    def incinerate_with_lasers():
        print("Wzzzuuuup!")


class Kick:

    @staticmethod
    def roundhouse_kick():
        print("Bump")


class SuperHero(ABC):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack

    @staticmethod
    def find(place):
        return place.get_antagonist()

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def ultimate(self):
        pass


class Superman(SuperHero, Laser):

    def __init__(self, can_use_ultimate_attack=True):
        super(Superman, self).__init__("Clark Kent", can_use_ultimate_attack)

    def attack(self):
        print("Kick")

    def ultimate(self):
        if self.can_use_ultimate_attack:
            self.incinerate_with_lasers()


class ChackNorris(SuperHero, Gun, Kick):

    def __init__(self, can_use_ultimate_attack=True):
        super(ChackNorris, self).__init__("Chack Norris", can_use_ultimate_attack)

    def attack(self):
        self.roundhouse_kick()

    def ultimate(self):
        if self.can_use_ultimate_attack:
            self.fire_a_gun()
