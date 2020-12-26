from Øving.oving_6.avl_tre_oving import *

class Student:
    def __init__(self, studentnummer, etternavn, fornavn, fodselsaar, studieretning, aarskurs):
        self.__studentnummer = studentnummer
        self.etternavn = etternavn
        self.fornavn = fornavn
        self.fodselsaar = fodselsaar
        self.studieretning = studieretning
        self.aarskurs = aarskurs

    @property
    def studentnummer(self):
        return self.__studentnummer

    def __str__(self):
        return f"Student {self.studentnummer}: {self.etternavn}, {self.fornavn}, går i {self.aarskurs}. årskurs {self.studieretning}"


def les_studentfil(fil_med_studenter):
    with open(fil_med_studenter) as fila:
        studentliste = []
        for linje in fila:
            attributter = linje.split("\t")
            studentliste.append(Student(int(attributter[0].strip()), attributter[1], attributter[2], int(attributter[3].strip()),
                                        attributter[4], int(attributter[5].strip())))
    return studentliste



if __name__ == "__main__":
    studentliste = les_studentfil("studenter.txt")
    for student in studentliste:
        print(student)

    print()
    tree = AVLTre()
    test = dict()

    for student in studentliste:
        tree[student.etternavn] = student
        test[student.studentnummer] = tree[student.etternavn]

    tree.skriv_treemap()
    print()
    print("Skriver ut treet i sortert rekkefølge på navn")
    v = tree.skriv_ut_rekursjon_inorder()
    print(v)
    print()
    for i in v:
        print(tree[i])

    print()
    print(tree["Nilsen"])
    print(test[1])