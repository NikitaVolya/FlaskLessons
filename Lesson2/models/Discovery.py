from models import PlanetModel

class Discovery:

    def __init__(self, planet: PlanetModel, year: int):
        self.__planet = planet
        self.__year = year

    @property
    def Planet(self):
        return self.__planet

    @property
    def Year(self):
        return self.__year

    def __str__(self):
        return f"{self.__planet.PlanetName} - {self.__year}"