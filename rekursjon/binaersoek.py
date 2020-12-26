# Binærsøk:
# - Sammenlikn det du leter etter med midten av lista
# - Hvis det du leter etter er større, sjekk slutten av lista
# - Hvis det du leter etter er mindre, sjekk starten av lista
# - Hvis det er likt har du funnet det
# - Har lista ett element igjen som er ulikt det du leter etter, finnes ikke elementet i lista
def binaersoek(sortert_liste, element):
    midten = len(sortert_liste)//2
    if sortert_liste[midten] == element:
        return midten
    if len(sortert_liste) == 1:
        return -1
    if sortert_liste[midten] < element:
        resultat = binaersoek(sortert_liste[midten:], element)
        if resultat == -1:
            return -1
        else:
            return midten + resultat
    if sortert_liste[midten] > element:
        return binaersoek(sortert_liste[:midten], element)

if __name__ == "__main__":
    liste = [2, 5, 6, 8, 15, 18, 23, 24, 26]
    print(binaersoek(liste, 8))
    print(binaersoek(liste, 25))
    print(binaersoek(liste, 26))
    print(binaersoek(liste, 2))