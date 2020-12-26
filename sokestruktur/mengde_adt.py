class Mengde:
    # Legger til en økkel hvis den ikke allerede der der
    def add(self, nokkel):
        pass

    # Sletter en nøkkel
    def delete(self, nokkel):
        pass

    # Henter ut nøkkelen
    def get(self, nokkel):
        pass

    # Inneholder mengden nøkkelen?
    def contains(self, nokkel):
        pass

    # Iterator

    # Returnere en ny mengde som inneholder både elmenete i denne mengden og elementene
    # i den oppgitte mengden.
    def union(self, mengde):
        pass

    # Returnere en nye mengde som inneholder elementene som er med i både self og
    # den oppgitte mengden
    def intersection(self, mengde):
        pass

    # Returnere en ny mengde som inneholder elementene som er med i self men ikke
    # i den oppgitte mengden
    def difference(self, mengde):
        pass

    # Delmengde: Returnere True hvis denne mengden inneholder alle elemente i den oppgitte
    # mengden, False ellers
    def subset(self, mengde):
        pass


# Mengde som holdes sortet på nøkkel
class SortedMengde (Mengde):
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