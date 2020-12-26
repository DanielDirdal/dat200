import random
import sortering.quicksort


def lag_tilfeldig_liste(lengde, rekkevidde=1000):
    liste = []
    for i in range(lengde):
        liste.append(random.randint(-rekkevidde, rekkevidde))
    return liste


def median_of_three_pivot(liste, startindex, sluttindex):
    sluttindex -= 1
    start_element = liste[startindex]
    slutt_element = liste[sluttindex]
    midt_index = (sluttindex + startindex)//2
    midt_element = liste[midt_index]
    if start_element <= midt_element and start_element <= slutt_element:
        if midt_element < slutt_element:
            return midt_index, midt_element
        else:
            return sluttindex, slutt_element
    if midt_element < start_element and midt_element <= slutt_element:
        if start_element < slutt_element:
            return startindex, start_element
        else:
            return sluttindex, slutt_element
    if slutt_element < midt_element and slutt_element < start_element:
        if midt_element < start_element:
            return midt_index, midt_element
        else:
            return startindex, start_element


def select(liste, posisjon, startindex=0, sluttindex=-1):
    # Forberedelse
    if sluttindex == -1:
        sluttindex = len(liste)

    # Basetilfelle
    if sluttindex - startindex <= 1:
        return liste[posisjon]
    if sluttindex - startindex == 2:
        if liste[startindex] > liste[sluttindex-1]:
            temp = liste[startindex]
            liste[startindex] = liste[sluttindex-1]
            liste[sluttindex-1] = temp
        return liste[posisjon]

    # Pivot valg
    pivot_index, pivot_element = median_of_three_pivot(liste, startindex, sluttindex)
    if pivot_index != startindex:
        temp = liste[startindex]
        liste[startindex] = pivot_element
        liste[pivot_index] = temp
    index_lavere = startindex+1     # S
    index_hoyere = sluttindex-1     # E

    # Splitter.
    # Indekser starter n unna hverandre og går 1 eller 2 nærmere hverandre for hver
    # iterasjon, så du får O(n) iterasjoner
    while index_lavere < index_hoyere:
        if liste[index_lavere] < pivot_element:
            index_lavere += 1
        elif liste[index_hoyere] > pivot_element:
            index_hoyere -= 1
        else:
            temp = liste[index_lavere]
            liste[index_lavere] = liste[index_hoyere]
            liste[index_hoyere] = temp
            index_lavere += 1
            index_hoyere -= 1

    # Setter inn pivot på riktig sted
    pivot_inn_index = index_lavere
    if liste[pivot_inn_index] > pivot_element:
        pivot_inn_index -= 1
    liste[startindex] = liste[pivot_inn_index]
    liste[pivot_inn_index] = pivot_element

    # Rekursiv splitt og hersk
    if posisjon == pivot_inn_index:
        return pivot_element
    if posisjon < pivot_inn_index:
        return select(liste, posisjon, startindex, pivot_inn_index)
    else:
        return select(liste, posisjon, pivot_inn_index+1, sluttindex)


if __name__ == "__main__":
    liste = lag_tilfeldig_liste(20, 30)
    print(liste)
    print("Minste element: ", select(liste, 0))
    print("3rd minste element: ", select(liste, 2))
    print("Median: ", select(liste, len(liste)//2))
    sortering.quicksort.sorter(liste)
    print(liste)
