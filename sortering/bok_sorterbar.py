class Bok:
    def __init__(self, ISBN, tittel, forfattere, utgivelsesaar):
        self.__ISBN = ISBN
        self.tittel = tittel
        self.forfattere = forfattere
        self.utgivelsesaar = utgivelsesaar

    # ISBN er read-only
    @property
    def ISBN(self):
        return self.__ISBN

    # Metode for å få ut en liste av forfattere som en streng
    def forfatterliste(self):
        resultat = ""
        for forfatter in self.forfattere:
            resultat += forfatter + ", "
        return resultat

    # String-metoden, sørger for at man kan lage en streng av boka
    def __str__(self):
        resultat = "Bok: " + self.tittel + " av " + self.forfatterliste()
        resultat += " utgitt i " + str(self.utgivelsesaar)
        return resultat

    # Sammenlikningsoperatorer for objekter. Her definerer jeg
    # tittel som nøkkel for bøker
    def __lt__(self, other):
        return self.tittel < other.tittel

    def __gt__(self, other):
        return self.tittel > other.tittel

    def __eq__(self, other):
        return self.tittel == other.tittel

    def __le__(self, other):
        return self.tittel <= other.tittel

    def __ge__(self, other):
        return self.tittel >= other.tittel

    def __ne__(self, other):
        return self.tittel != other.tittel
