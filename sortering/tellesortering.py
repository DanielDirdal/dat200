import random

def lag_tilfeldig_liste(lengde, rekkevidde = 1000):
    liste = []
    for i in range(lengde):
        liste.append(random.randint(-rekkevidde,rekkevidde))
    return liste

# Kjøretid: Theta(n + verdiområde)
# Minnebruk: Theta(n + verdiområde)
def tellesortering(liste, verdi_min, verdi_maks):
    # Kan gå gjennom lista for å finne minimum og maksimum for å finne verdiområdet
    antall_hver_verdi = []
    for i in range(1+verdi_maks-verdi_min):             # Hadde jeg brukt en numpy array hadde den gått i O(1)
        antall_hver_verdi.append(0)
    for element in liste:                               # Theta(n)
        antall_hver_verdi[element-verdi_min] += 1
    posisjon_hver_verdi = []
    posisjon_hver_verdi.append(0)
    for i in range(1, 1+verdi_maks-verdi_min):          # Theta(verdiområde)
        posisjon_hver_verdi.append(antall_hver_verdi[i-1] + posisjon_hver_verdi[i-1])
    resultat_liste = []
    for i in range(len(liste)):                         # Theta(n)
        resultat_liste.append(0)
    for element in liste:                               # Theta(n)
        resultat_liste[posisjon_hver_verdi[element-verdi_min]] = element
        posisjon_hver_verdi[element-verdi_min] += 1
    return resultat_liste


if __name__ == "__main__":
    liste = lag_tilfeldig_liste(20, 10)
    print(liste)
    liste = tellesortering(liste, -10, 10)
    print(liste)