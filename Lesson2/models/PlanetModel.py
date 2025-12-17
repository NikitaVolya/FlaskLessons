

class PlanetModel:

    def __init__(self, planetName: str, description: str, satellitesNumber: int):
        self.__planetName = planetName
        self.__description = description
        self.__satellitesNumber = satellitesNumber

    @property
    def PlanetName(self):
        return self.__planetName

    @property
    def Description(self):
        return self.__description

    @property
    def SatellitesNumber(self):
        return self.__satellitesNumber

    @property
    def HasManySatellites(self):
        return self.__satellitesNumber > 10