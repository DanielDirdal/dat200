import random

# Kjøretid
# Worst case O(n^2) - lista er sortert i motsatt rekkefølge
# Best case O(n) - lista er allerde sortert
# Average case: O(n^2)
#
# Minnebruk: Theta(1)
def sorter(liste):
    for element in range(1, len(liste)):                            # Theta(n)
        index = element                                             # Theta(n)
        while liste[index] < liste[index-1] and index > 0:          # Worst case går tilbake til starten hver gang
                                                                    # Best case sammenlikningen slår aldri til
            temp = liste[index]
            liste[index] = liste[index-1]
            liste[index-1] = temp
            index -= 1

def lag_tilfeldig_liste(lengde):
    liste = []
    for i in range(lengde):
        liste.append(random.randint(-1000,1000))
    return liste

if __name__ == "__main__":
    liste = lag_tilfeldig_liste(10)
    print(liste)
    sorter(liste)
    print(liste)