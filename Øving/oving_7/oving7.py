from Øving.oving_7.student import *
from Øving.oving_7.emne import *
from Øving.oving_7.eksamensresultat import *
from Øving.oving_6.avl_tre_oving import *


def finn_student(studentnr, studentliste):
    for student in studentliste:
        if student.studentnummer == studentnr:
            return student
    return None


def finn_emne(emnekode, emneliste):
    for emne in emneliste:
        if emne.emnekode == emnekode:
            return emne
    return None


def les_eksamensresultater(studentliste, emneliste):
    eksamensliste = []
    with open("eksamensresultater.txt") as eksamens_fil:
        for linje in eksamens_fil:
            atributter = linje.split("\t")
            studenten = finn_student(int(atributter[0].strip()), studentliste)
            emnet = finn_emne(atributter[1].strip(), emneliste)
            nytt_eksamensresultat = Eksamensresultat(studenten, emnet, atributter[2].strip())
            eksamensliste.append(nytt_eksamensresultat)
    return eksamensliste

def les_eksamensresultater_ny(hashmap, avl_tre_emner):
    eksamensliste = []
    with open("eksamensresultater.txt") as eksamens_fil:
        for linje in eksamens_fil:
            atributter = linje.split("\t")
            studenten = hashmap[int(atributter[0].strip())]
            emnet = avl_tre_emner[atributter[1].strip()]
            nytt_eksamensresultat = Eksamensresultat(studenten, emnet, atributter[2].strip())
            eksamensliste.append(nytt_eksamensresultat)
    return eksamensliste

def skriv_ut_data_om_student(tre):
    verdi = input("Skriv inn navnet til student du vil ha data om: ")
    if verdi in tre:
            return tre[verdi]
    return f"Personen {verdi} finnes ikke i AVLTreet"

def skriv_ut_data_om_et_emne(hashmap):
    verdi = input("Skriv inn emnekoden til et emne du vil ha data om: ")
    if verdi in hashmap:
            return hashmap[verdi]
    return f"Emnekoden: {verdi} finnes ikke i hashmappet"

if __name__ == "__main__":
    studentliste = les_studentfil("studenter.txt")
    emneliste = les_emner("Emner.txt")
    eksamensliste = les_eksamensresultater(studentliste, emneliste)


    for eksamensresultat in eksamensliste:
        print(eksamensresultat)


    # Lager hashmap som dictionary og avl_tre likt som i øving 6
    hashmap_emner = dict()
    avl_tre_studener = AVLTre()
    hashmap_studenter_paa_studentnummer = dict()

    print()
    for student in studentliste:
        avl_tre_studener[student.etternavn] = student
        hashmap_studenter_paa_studentnummer[int(student.studentnummer)] = student
    print()
    avl_tre_studener.skriv_treemap()
    print("Skriver ut AVLTreet i sortert rekkefølge: ")
    v = avl_tre_studener.skriv_ut_rekursjon_inorder()
    print(v)
    print()
    for i in v:
        print(avl_tre_studener[i])
    print()
    print("Tester ut studentnummer for Nilsen : ", end="")
    print(avl_tre_studener["Nilsen"].studentnummer)
    print()
    person = skriv_ut_data_om_student(avl_tre_studener)
    print(person)


    print()
    for emne in emneliste:
        hashmap_emner[emne.emnekode] = emne
    for emne in hashmap_emner:
        print(hashmap_emner[emne])
    print()
    emne = skriv_ut_data_om_et_emne(hashmap_emner)
    print(emne)



    print()
    skriv_ut = input("Vil du skrive ut eksamensresultatene på ny skriv: ja")
    eksamensliste_ny = les_eksamensresultater_ny(hashmap_studenter_paa_studentnummer, hashmap_emner)
    if skriv_ut == "ja":
        for resultat in eksamensliste_ny:
            print(resultat)
