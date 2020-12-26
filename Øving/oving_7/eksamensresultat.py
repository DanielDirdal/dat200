class Eksamensresultat:
    def __init__(self, student, emne, karakter):
        self.__student = student
        self.__emne = emne
        self.karakter = karakter

    @property
    def student(self):
        return self.__student

    @property
    def emne(self):
        return self.__emne

    def __str__(self):
        return f"Studenten {self.student.etternavn}, {self.student.fornavn} har karakteren {self.karakter} i emnet {self.emne.emnenavn}"
