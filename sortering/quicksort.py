import random

def lag_tilfeldig_liste(lengde, rekkevidde = 1000):
    liste = []
    for i in range(lengde):
        liste.append(random.randint(-rekkevidde,rekkevidde))
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
    if slutt_element < start_element and slutt_element < midt_element:
        if midt_element < start_element:
            return midt_index, midt_element
        else:
            return startindex, start_element

def sorter(liste, startindex=0, sluttindex=-1):
    # Forberedelse
    if sluttindex == -1:
        sluttindex = len(liste)

    # Basetilfelle
    if sluttindex - startindex <= 1:
        return
    if sluttindex - startindex == 2:
        if liste[startindex] > liste[sluttindex-1]:
            temp = liste[startindex]
            liste[startindex] = liste[sluttindex-1]
            liste[sluttindex-1] = temp
        return

    # Pivot valg
    pivot_index, pivot_element = median_of_three_pivot(liste, startindex, sluttindex)
    if pivot_index != startindex:
        temp = liste[startindex]
        liste[startindex] = pivot_element
        liste[pivot_index] = temp
    index_lavere = startindex+1             # S
    index_hoyere = sluttindex-1             # E

    # Splitter
    # Indekser starter n unna hverandre og 1 eller 2 nærmere hverandre for hver
    # iterasjon, så du får O(n) iterasjoner.
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

    print(liste[startindex:sluttindex])
    print(f"Pivot element {pivot_element}")
    print(liste[startindex:pivot_inn_index])
    print(liste[pivot_inn_index+1:sluttindex])

    # Rekursiv splitt og hersk
    sorter(liste, startindex, pivot_inn_index)
    sorter(liste, pivot_inn_index+1, sluttindex)

if __name__ == "__main__":
    #liste = lag_tilfeldig_liste(20, 30)
    #print(liste)
    #sorter(liste)
    #print(liste)
    #print()

    liste2 = [-20, 8, -3, -16, 9, 14, 1, -8, -17, 5]
    print(liste2)
    sorter(liste2)
    print(liste2)