from Øving.oving_6.avl_tre_oving import *

class Emne:
    def __init__(self, emnekode, emnenavn, semester, studiepoeng):
        self.__emnekode = emnekode
        self.emnenavn = emnenavn
        self.semester = semester
        self.studiepoeng = studiepoeng

    @property
    def emnekode(self):
        return self.__emnekode

    def __str__(self):
        return f"Emne {self.emnekode} - {self.emnenavn}. Semester: {self.semester}. Antall studiepoeng: {self.studiepoeng}."


def les_emner(emne_fil):
    emner = []
    with open(emne_fil) as fila:
        for linje in fila:
            atributter = linje.split("\t")
            emner.append(Emne(atributter[0].strip(), atributter[1].strip(), atributter[2].strip(), int(atributter[3].strip())))
    return emner



if __name__ == "__main__":
    emner = les_emner("emner.txt")
    for emne in emner:
        print(emne)

    emne_map = dict()
    print()
    for emne in emner:
        emne_map[emne.emnekode] = emne

    for emne in emne_map:
        print(emne_map[emne])

    print()
    skriv_ut_emne = input("Skriv ut data om et emne på emnekode: ")

    if skriv_ut_emne in emne_map:
        print(emne_map[skriv_ut_emne])
    else:
        print(f"Feil {skriv_ut_emne} finnes ikke")
