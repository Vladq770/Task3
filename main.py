from typing import Union
from heroes import Superman, ChackNorris, SuperHero
from places import City, Planet
from news import News


def save_the_place(hero: SuperHero, place: Union[City, Planet]):
    hero.find(place)
    hero.attack()
    hero.ultimate()
    News.create_news(place, hero)


if __name__ == '__main__':
    Kostroma = City("Kostroma", "Orcs hid in the forest")
    Tokyo = City("Tokyo", "Godzilla stands near a skyscraper")
    save_the_place(Superman(), Kostroma)
    print('-' * 20)
    save_the_place(ChackNorris(False), Tokyo)
    Earth = Planet([123, 124, 1325], "Aliens from Mars")
    print('-' * 20)
    save_the_place(ChackNorris(True), Earth)
