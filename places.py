from abc import ABC, abstractmethod


class Place(ABC):

    @abstractmethod
    def get_antagonist(self):
        pass


class City(Place):

    def __init__(self, name, antagonist):
        self.name = name
        self.antagonist = antagonist

    def get_antagonist(self):
        print(self.antagonist)


class Planet(Place):

    def __init__(self, coordinates, antagonist):
        self.coordinates = coordinates
        self.antagonist = antagonist

    def get_antagonist(self):
        print(self.antagonist)
