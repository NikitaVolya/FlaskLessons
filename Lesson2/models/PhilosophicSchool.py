
"""
Вирішив спробувати зробити щось схоже на моделі з .Net
"""
class PhilosophicSchool:

    __globalId = 0

    def __init__(self, schoolName: str):
        self.__id = PhilosophicSchool.__globalId
        self.__schoolName = schoolName

        PhilosophicSchool.__globalId += 1

    @property
    def Id(self):
        return self.__id

    @property
    def SchoolName(self):
        return self.__schoolName
