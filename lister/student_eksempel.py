class Student:
    def __init__(self, navn, studieretning, aarskurs):
        self.navn = navn
        self.studieretning = studieretning
        self.aarskurs = aarskurs

    @property
    def aarskurs(self):
        return self.__aarskurs

    @aarskurs.setter
    def aarskurs(self, nytt_aarskurs):
        if nytt_aarskurs < 1:
            raise ValueError("Kan ikke ha årskurs under 1!")
        if nytt_aarskurs > 5:
            raise ValueError("Kan ikke ha årskurs høyere enn 5!")
        self.__aarskurs = nytt_aarskurs

    def __str__(self):
        return f"Student: {self.navn} går i {self.aarskurs} årskurs {self.studieretning}"

if __name__ == "__main__":
    variabel = 8
    test = Student("Arne Andresen", "Data", 2)
    print(test)
    test2 = Student("Marit Berg", "Data", 1)
    print(test2)
    print(variabel)