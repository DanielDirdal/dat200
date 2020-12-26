import datetime
from Øving.oving_6.avl_tre_oving import *

class Vindmaaling:
    neste_id = 1

    def __init__(self, tidspunkt, vindstyrke):
        self.__tidspunkt = tidspunkt
        self.__vindstyrke = vindstyrke
        self.__id = Vindmaaling.neste_id
        Vindmaaling.neste_id += 1

    def get_tidspunkt(self):
        return self.__tidspunkt

    def get_vindstyrke(self):
        return self.__vindstyrke

    def get_id(self):
        return self.__id

    def __str__(self):
        return f"Vindmåling {self.__id}. Tidspunkt: {self.__tidspunkt}. Vindstyrke: {self.__vindstyrke}"

    def __lt__(self, other):
        return self.__tidspunkt < other.get_tidspunkt()


def les_vindmaalinger(filnavn):
    vindmaalinger = []
    with open(filnavn, "r") as fila:
        for linje in fila:
            linje.strip()
            komponenter = linje.split("\t")
            tidspunkt = datetime.datetime.fromisoformat(komponenter[1])
            vindstyrke = float(komponenter[3])
            ny_maaling = Vindmaaling(tidspunkt, vindstyrke)
            vindmaalinger.append(ny_maaling)
    return vindmaalinger


if __name__ == "__main__":
    vindmaalinger = les_vindmaalinger("vindmaalinger_redusert_mer.txt")
    print(len(vindmaalinger))
    print(vindmaalinger[0])
    print(vindmaalinger[1000])
    print(vindmaalinger[-1])
    map = AVLTre()
    for i in range(len(vindmaalinger)):
        map[vindmaalinger[i].get_tidspunkt()] = vindmaalinger[i].get_vindstyrke()

    print()
    if map[datetime.datetime.fromisoformat("2010-12-04 12:00:00")] != 0:
        print(map[datetime.datetime.fromisoformat("2010-12-04 12:00:00")])
    else:
        print("Så bruker neste verdi istede då: ", end='')
        print(map.next(datetime.datetime.fromisoformat("2010-12-04 12:00:00")), end=' med vindstyrke: ')
        verdi = map.next(datetime.datetime.fromisoformat("2010-12-04 12:00:00"))
        print(map[verdi])

    print()
    liste = map.between(datetime.datetime.fromisoformat("2011-12-07 00:00:00"), datetime.datetime.fromisoformat("2011-12-08 00:00:00"))
    maks = 0
    for i in liste:
        if map[i] > maks:
            maks = map[i]
    print(f"Maks vindstryke på dagen 2011-12-07 er: {maks}")