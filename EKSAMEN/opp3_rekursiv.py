def rekursiv_funksjon(liste, start=0, slutt=-1):
    if slutt == -1:
        slutt = len(liste)
    if slutt - start == 0:
        return 0
    if slutt - start == 1:
        return liste[start]
    if slutt - start == 2:
        return liste[start] + liste[slutt-1]
    return rekursiv_funksjon(liste, start, (start + slutt) // 2) + rekursiv_funksjon(liste, (start + slutt) // 2, slutt)

if __name__ == "__main__":
    liste = [-3, 5, -2, 10]
    print(rekursiv_funksjon(liste, 1, 3))