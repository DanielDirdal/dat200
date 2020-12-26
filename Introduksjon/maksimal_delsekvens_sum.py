import random
import time

def lag_tilfeldig_liste(lengde):
    liste = []
    for i in range(lengde):
        liste.append(random.randint(-1000,1000))
    return liste


# Start med å sjekke alle mulighetene, "brute force algoritme"
# Lag en variabel som inneholder foreløpig høest sum, kan starte lik det første elementet
# For hvert startelement i lista
#   For hvert sluttelement etter startelement
#       Lag en teller som sier foreløping sum
#       For hvert element i delsekvensen
#           Legg tallet til summen
#       Sjekk om summen er høyest og oppdater variabelen hvis ikke

#Kjøretid O(n**3)
def maksimal_delsekvens_sum_kubisk(liste):
    if len(liste) == 0:                                     # Kjører 1 gang
        return 0                                            # Kjører 1 gang
    hoyeste_sum = liste[0]                                  # Kjører 1 gang
    for start in range(len(liste)):                         # Kjører n ganger
        for slutt in range(start, len(liste)):              # Kjører O(n**2)
            teller = 0                                      # Kjører O(n**2)
            for index in range(start, slutt):               # Kjører O(n**3)
                teller += liste[index]                      # Kjører O(n**3)
            if teller > hoyeste_sum:                        # Kjører O(n**3)
                hoyeste_sum = teller                        # best case 1, worst case O(n**3)
    return hoyeste_sum                                      # Kjører 1 gang


# Start med å sjekke alle mulighetene
# Lag en variabel som inneholder foreløpig høest sum, kan starte lik det første elementet
# For hvert startelement i lista
#   Lag en teller som sier foreløping sum
#   For hvert sluttelement etter startelement
#       Legg elementet til telleren
#       Sjekk om summen er høyest og oppdater variabelen hvis ikke


def maksimal_delsekvens_sum_kvadratisk(liste):
    if len(liste) == 0:                                     # Kjører 1 gang
        return 0                                            # Kjører 1 gang
    hoyeste_sum = liste[0]                                  # Kjører 1 gang
    for start in range(len(liste)):                         # Kjører n ganger
        teller = 0                                          # Kjører n ganger
        for slutt in range(start, len(liste)):              # Kjører O(n**2)
            teller += liste[slutt]                          # Kjører O(n**2)
            if teller > hoyeste_sum:                        # Kjører O(n**2)
                hoyeste_sum = teller                        # best case 1, worst case O(n**2)
    return hoyeste_sum                                      # Kjører 1 gang


# Obervasjon 1: Gitt en delsekvens E(i->j) med sum S(i->j) < 0. For en hver sekvens E(i->p)
# , p > j: S(i->p) <= S(j->P)

# Obeservasjon 2: Alle delsekvenser som grenser til den maksimale må ha negativ sum. Ellers hadde
# de vært med i den maksimale!

# Observasjon 3: For en hver j, la S(i->j) være den første delsekvensen med negativ sum.
# Gitt en p mellom i og j og en q>j. Da er S(p->q) enten ikke maksimal eller lik en annen
# maksimal delsekvens. Hvis p=i, se observasjon 1. Siden j er den første indeksen hvor summen
# er negativ, så er S(i->p) >= 0. Så S(i->q) >= S(p->q). For alle q>j, så gir observasjon 1
# at S(i->q) ikke er maksimal.

# Maksimal delsekvens sum lineær
# Lag en teller som startet på 0
# Lag en maksverdi lik første element i lista
# For hvert element i lista
#   Legg element til telleren
#   Hvis teller < 0, sett den lik 0
#   Hvis teller høyere enn maksverdi, sett maksverdi lik teller
# Return maksverdi

def maksimal_delsekvens_sum_linear(liste):
    if len(liste) == 0:                             # Kjører 1 gang
        return 0                                    # Kjører 1 gang
    hoyeste_sum = liste[0]                          # Kjører 1 gang
    teller = 0                                      # Kjører 1 gang
    for element in liste:                           # Kjører n ganger
        teller += element                           # Kjører n ganger
        if teller > hoyeste_sum:                    # Kjører n ganger
            hoyeste_sum = teller                    # Kjører maksimalt n ganger
        if teller < 0:                              # Kjører n ganger
            teller = 0                              # Kjører maksimalt n ganger
    return hoyeste_sum                              # Kjører 1 gang

if __name__ == "__main__":
    liste = [2, -4, 6, 2, 3, -8, -4, -2, 5, -4, 6, 4, 3, -8, -10]
    print(maksimal_delsekvens_sum_kubisk(liste))
    print(maksimal_delsekvens_sum_kvadratisk(liste))
    print(maksimal_delsekvens_sum_linear(liste))

    liste2 = lag_tilfeldig_liste(500)

    tid_start = time.process_time()
    print(maksimal_delsekvens_sum_kubisk(liste2))
    tid_slutt = time.process_time()
    print(f"Tid kubisk 500 elementer: {tid_slutt-tid_start}")

    tid_start = time.process_time()
    print(maksimal_delsekvens_sum_kvadratisk(liste2))
    tid_slutt = time.process_time()
    print(f"Tid kvadratisk 500 elementer: {tid_slutt - tid_start}")

    tid_start = time.process_time()
    print(maksimal_delsekvens_sum_linear(liste2))
    tid_slutt = time.process_time()
    print(f"Tid lineær 500 elementer: {tid_slutt - tid_start}")