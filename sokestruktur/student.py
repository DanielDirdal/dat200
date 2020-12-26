class Student:
    neste_id = 1

    def __init__(self, fornavn, etternavn, studieprogram, aarskurs=1):
        self.__id = Student.neste_id
        Student.neste_id += 1
        self.__fornavn = fornavn
        self.__etternavn = etternavn
        self.__studieprogram = studieprogram
        self.__aarskurs = aarskurs

    def get_fornavn(self):
        return self.__fornavn

    def get_etternavn(self):
        return self.__etternavn

    def get_studentnummer(self):
        return self.__id

    def get_studieprogram(self):
        return self.__studieprogram

    def get_aarskurs(self):
        return self.__aarskurs

    def __lt__(self, other):
        if self.__etternavn < other.get_etternavn():
            return True
        if self.__etternavn > other.get_etternavn():
            return False
        return self.__fornavn < other.get_fornavn()

    def __le__(self, other):
        if self.__etternavn < other.get_etternavn():
            return True
        if self.__etternavn > other.get_etternavn():
            return False
        return self.__fornavn <= other.get_fornavn()

    def __eq__(self, other):
        return self.__etternavn == other.get_etternavn() \
               and self.__fornavn == other.get_fornavn()

    def __hash__(self):
        return hash(self.__etternavn) + hash(self.__fornavn)

    def __gt__(self, other):
        if self.__etternavn > other.get_etternavn():
            return True
        if self.__etternavn < other.get_etternavn():
            return False
        return self.__fornavn > other.get_fornavn()

    def __ge__(self, other):
        if self.__etternavn > other.get_etternavn():
            return True
        if self.__etternavn < other.get_etternavn():
            return False
        return self.__fornavn >= other.get_fornavn()

    def __ne__(self, other):
        if self.__etternavn != other.get_etternavn():
            return True
        return self.__fornavn != other.get_fornavn()

    def __str__(self):
        return self.__fornavn + " " + self.__etternavn + \
               " som går i " + str(self.__aarskurs) + \
               " " + self.__studieprogram


def lag_student_liste():
    liste = []
    liste.append(Student("Arne", "Nilsen", "Data", 2))
    liste.append(Student("Marit", "Hansen", "Data", 2))
    liste.append(Student("Ole", "Vik", "Data", 2))
    liste.append(Student("Daniel", "Herrem", "Data", 2))
    liste.append(Student("Ida", "Ytrebø", "Data", 2))
    liste.append(Student("Eirik", "Bø", "Elektro", 2))
    liste.append(Student("Georg", "Olavsen", "Elektro", 2))
    liste.append(Student("Anne", "Nilsen", "Elektro", 2))
    liste.append(Student("Hilde", "Erlingsen", "Elektro", 2))
    return liste
