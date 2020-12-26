from sokestruktur import student as std
class SortetListeMap:
    def __init__(self):
        self.liste = []

    # Variant av binærsøk som søker på nøkkel og som returnere to verdier,
    # indeksen den finner og om den fant det eller ikke
    #
    # Kjøretid: O(log(n))
    def binaersoek(self, element, sortert_liste=None):
        if sortert_liste is None:
            sortert_liste = self.liste
        midten = len(sortert_liste) // 2
        if sortert_liste[midten][0] == element:
            return midten, True
        if len(sortert_liste) == 1:
            return 0, False
        if sortert_liste[midten][0] < element:
            resultat, funnet = self.binaersoek(element, sortert_liste[midten:])
            return midten + resultat, funnet
        if sortert_liste[midten][0] > element:
            return self.binaersoek(element, sortert_liste[:midten])

    # Setter inn en oppgit nokkel med oppgit verdi, overskriver gammel verdi
    # hvis nøkkelen allerede ligger der
    #
    # Kjøretid: O(log(n)) hvis elemente allerede er i lista
    #           O(n) hvis elemente ikke er i lista
    def put(self, nokkel, verdi):
        # Finn ut hvor det skal settes inn
        # Bruk insert for å sette det inn der
        liste_element = (nokkel, verdi)
        if len(self.liste) == 0:
            self.liste.append(liste_element)
        index, funnet = self.binaersoek(nokkel)
        if funnet:
            self.liste[index] = liste_element
        else:
            if nokkel > self.liste[index][0]:
                index += 1
            self.liste.insert(index, liste_element)

    def __setitem__(self, key, value):
        self.put(key, value)

    # Henter ut verdien for oppgitt nøkkel
    #
    # Kjøretid: O(log(n))
    def get(self, nokkel):
        # Gjør binærsøk på nøkkel for å finne den
        if len(self.liste) == 0:
            raise KeyError("Map-et er tomt!")
        index, funnet = self.binaersoek(nokkel)
        if funnet:
            return self.liste[index][1]
        else:
            raise KeyError(f"Finner ikke nøkkelen {nokkel}")

    def __getitem__(self, key):
        return self.get(key)

    # Fjerne en nøkkel fra map-et. Fjener også verdien.
    #
    # Kjøretid: Hvis det ikke er i lista O(log(n))
    #           Hvis det er i lista O(n)
    def delete(self, nokkel):
        # Gjør et binærsøk for å finne det
        # Bruk del kommandoen for å fjerne det
        if len(self.liste) > 0:
            index, funnet = self.binaersoek(nokkel)
            if funnet:
                del self.liste[index]


    # Finnes nøkkelen i samlingen
    #
    # Kjøretid: O(log(n))
    def contains(self, nokkel):
        # Gjør et binærsøk for å finne det
        if len(self.liste) == 0:
            return False
        index, funnet = self.binaersoek(nokkel)
        return funnet

    def __contains__(self, nokkel):
        return self.contains(nokkel)

    # Iterator: Trenger en iterator som returnere nøkler slik at man kan bruke
    # en for-loop til å gå gjennom alle nøklene i samlingen.
    def __iter__(self):
        return SortetMapIterator(self)


    # Hent første nøkkel som er større en oppgitt nøkkel hvis det fines en slik
    #
    # Kjøretid O(log(n))
    def next(self, nokkel):
        if len(self.liste) == 0:
            raise KeyError("Map-et er tomt!")
        index, funnet = self.binaersoek(nokkel)
        if funnet:
            index += 1
            if index >= len(self.liste):
                return None
            return self.liste[index][0]
        else:
            if self.liste[index][0] < nokkel:
                index += 1
                if index >= len(self.liste):
                    return None
            return self.liste[index][0]

    # Henter ut første nøkkel som er mindre
    #
    # Kjøretid O(log(n))
    def previous(self, nokkel):
        if len(self.liste) == 0:
            raise KeyError("Map-et er tomt!")
        index, funnet = self.binaersoek(nokkel)
        if funnet:
            index -= 1
            if index < 0:
                return None
            return self.liste[index][0]
        else:
            if self.liste[index][0] < nokkel:
                index -= 1
                if index < 0:
                    return None
            return self.liste[index][0]

    # Henter ut den laveste nøkkelen
    #
    # Kjøretid O(1)
    def first(self):
        if len(self.liste) == 0:
            raise KeyError("Map-et er tomt!")
        return self.liste[0][0]

    # henter ut den høyeste nøkkelen
    #
    # Kjøretid O(1)
    def last(self):
        if len(self.liste) == 0:
            raise KeyError("Map-et er tomt!")
        return self.liste[-1][0]

    # Hent ut alle nøkler mellom to oppgitte nøkler
    #
    # Kjøretid: O(log(n) + antall elementer i resultatet)
    def between(self, forste, siste):
        resultat = []
        if len(self.liste) == 0:
            raise KeyError("Map-et er tomt!")
        index, funnet = self.binaersoek(forste)
        if self.liste[index][0] < forste:
            index += 1
        while index <= len(self.liste) and self.liste[index][0] < siste:
            resultat.append(self.liste[index][0])
            index += 1
        return resultat

    # Finn det k-ende nøkkel, Selection problemet
    #
    # O(1)
    def finn_k_ende(self, k):
        if len(self.liste) == 0:
            raise KeyError("Map-et er tomt!")
        return self.liste[k][0]

    # Kjøretid O(n)
    def skriv_ut_liste(self):
        for index, element in enumerate(self.liste):
            print(f"{index}: {element}")

class SortetMapIterator:
    def __init__(self, map_et):
        self.map_et = map_et
        self.index = 0

    # Kjøretid: O(1)
    # Gå gjennom hele lista O(n)
    def __next__(self):
        if self.index >= len(self.map_et.liste):
            raise StopIteration
        nokkel = self.map_et.liste[self.index][0]
        self.index += 1
        return nokkel

    def __iter__(self):
        return self

if __name__ == "__main__":
    studentliste = std.lag_student_liste()
    map = SortetListeMap()
    for student in studentliste:
        map.put(student.get_etternavn(), student)
    map.skriv_ut_liste()
    print(map.get("Vik"))
    print(map.get("Nilsen"))
    map.delete("Vik")
    map.skriv_ut_liste()
    print(map.contains("Erlingsen"))
    print(map.contains("Ås"))
    print()
    for nokkel in map:
        print(nokkel)
    print()
    print(map.next("F"))
    print(map.next("Nilsen"))
    print()
    print(map.previous("F"))
    print(map.previous("Nilsen"))
    print()
    print(map.first())
    print(map.last())
    print()
    print(map.between("D", "M"))
    print(map.finn_k_ende(3))