class Map:
    # Setter inn en oppgit nokkel med oppgit verdi, overskriver gammel verdi
    # hvis nøkkelen allerede ligger der
    def put(self, nokkel, verdi):
        pass

    def __setitem__(self, key, value):
        self.put(key, value)

    # Henter ut verdien for oppgitt nøkkel
    def get(self, nokkel):
        pass

    def __getitem__(self, key):
        return self.get(key)

    # Fjerne en nøkkel fra map-et. Fjener også verdien.
    def delete(self, nokkel):
        pass

    # Finnes nøkkelen i samlingen
    def contains(self, nokkel):
        pass

    def __contains__(self, nokkel):
        return self.contains(nokkel)

    # Iterator: Trenger en iterator som returnere nøkler slik at man kan bruke
    # en for-loop til å gå gjennom alle nøklene i samlingen.

# Map som holdes sortet på nøkkel
class SortedMap (Map):
    # Hent første nøkkel som er større en oppgitt nøkkel hvis det fines en slik
    def next(self, nokkel):
        pass

    # Henter ut første nøkkel som er mindre
    def previous(self, nokkel):
        pass

    # Henter ut den laveste nøkkelen
    def first(self):
        pass

    # henter ut den høyeste nøkkelen
    def last(self):
        pass

    # Hent ut alle nøkler mellom to oppgitte nøkler
    def between(selfself, forste, siste):
        pass

    # Finn det k-ende element, Selection problemet
    def finn_k_ende(self, k):
        pass
