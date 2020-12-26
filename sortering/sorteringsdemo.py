import random
import time
import sortering.innsettingssortering
import sortering.shellsort
import sortering.flettesortering
import sortering.quicksort

def lag_tilfeldig_liste(lengde, rekkevidde = 1000):
    liste = []
    for i in range(lengde):
        liste.append(random.randint(-rekkevidde,rekkevidde))
    return liste


# Kjøretid O(n)
def lista_sorter(liste):
    for index in range(len(liste) - 1):
        if liste[index] > liste[index +1 ]:
            return False
    return True

if __name__ == "__main__":
    liste = lag_tilfeldig_liste(5000, 5000)

    liste2 = liste[:]
    print(lista_sorter(liste2))
    tid_start = time.process_time()
    sortering.innsettingssortering.sorter(liste2)
    tid_slutt = time.process_time()
    print(f"Tid innsettingssortering 5000 elementer: {tid_slutt - tid_start}")
    print(lista_sorter(liste2))
    print("\n")

    liste2 = liste[:]
    print(lista_sorter(liste2))
    tid_start = time.process_time()
    sortering.shellsort.sorter(liste2)
    tid_slutt = time.process_time()
    print(f"Tid shellsort 5000 elementer: {tid_slutt - tid_start}")
    print(lista_sorter(liste2))
    print("\n")

    liste2 = liste[:]
    print(lista_sorter(liste2))
    tid_start = time.process_time()
    liste2 = sortering.flettesortering.flettesortering_bytter_algoritme(liste2)
    tid_slutt = time.process_time()
    print(f"Tid flettesortering 5000 elementer: {tid_slutt - tid_start}")
    print(lista_sorter(liste2))
    print("\n")

    liste2 = liste[:]
    print(lista_sorter(liste2))
    tid_start = time.process_time()
    sortering.quicksort.sorter(liste2)
    tid_slutt = time.process_time()
    print(f"Tid quicksort 5000 elementer: {tid_slutt - tid_start}")
    print(lista_sorter(liste2))
    print("\n")