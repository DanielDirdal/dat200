import random

def lag_tilfeldig_liste(lengde, rekkevidde = 1000):
    liste = []
    for i in range(lengde):
        liste.append(random.randint(-rekkevidde,rekkevidde))
    return liste

# Kjøretid O(n^1,5), average case, O(n^2) worst case
# Minnebruk O(1)
def k_sorter(liste, k):
    for i in range(0, k):
        for element in range(k+i, len(liste), k):
            index = element
            while liste[index] < liste[index - k] and index >= k:
                temp = liste[index]
                liste[index] = liste[index - k]
                liste[index - k] = temp
                index -= k

def sorter(liste):
    k = len(liste)//2
    if k%2 == 0:
        k +=1
    while k > 1:
        k_sorter(liste, k)
        k = k//2
        if k%2 == 0:
            k += 1
    k_sorter(liste, 1)



if __name__ == "__main__":
    liste = lag_tilfeldig_liste(12, 20)
    print(liste)
    sorter(liste)
    print(liste)
    print()
    liste2 = [-20, 8, -3, -16, 9, 14, 1, -8, -17, 5]
    print(liste2)
    k_sorter(liste2, 5)
    print(liste2)
    k_sorter(liste2, 3)
    print(liste2)
    k_sorter(liste2, 2)
    print(liste2)