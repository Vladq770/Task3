from places import City, Planet


class News:

    @staticmethod
    def create_news(place, hero):
        if isinstance(place, City):
            print(f'{hero.name} saved the {place.name}!')
        elif isinstance(place, Planet):
            print(f'{hero.name} saved the planet with coordinates {place.coordinates}!')
