# Geometrisk rekke: ao*r**n
# Eksempel 1*2**n = 1, 2, 4, 8, 16, 32 ,64 ...
# Antall verdier for at en løkke skal avslutte

class GeometriskRekke:
    def __init__(self, a0, r, antall_verdier):
        self.a0 = a0
        self.r = r
        self.antall_verdier = antall_verdier

    def __getitem__(self, item):
        if item > self.antall_verdier:
            raise IndexError(f"Indeksen {item} er for stor! Maksgrense er {self.antall_verdier-1}")
        return self.a0*self.r**item

    def __iter__(self):
        return GeometriskRekkeIterator(self)

class GeometriskRekkeIterator:
    def __init__(self, rekka):
        self.rekka = rekka
        self.nv_element = 0

    def __next__(self):
        if self.nv_element >= self.rekka.antall_verdier:
            raise StopIteration
        resultat = self.rekka[self.nv_element]
        self.nv_element += 1
        return resultat

    def __iter__(self):
        return self

if __name__ == "__main__":
    toere = GeometriskRekke(4, 2, 16)
    print(toere[1])             # toere[1] oversettes til toere.__getitem__(1)
    print(toere[5])             # toere[5] oversettes til toere.__getitem__(5)
    for element in toere:
        print(element)


# __setitem__(self, item, verdi) tilsvarer liste[item] = verdi,
# liste[item] = verdi oversettes til liste.__setitem__(item, verdi)

# __delitem__(self, item) tilsvarer "del liste[item]"

# __contain__(self, element) brukes for å evaluere in-operatoren, "if element in liste: "
#       oversettes til "if liste.__contain__(element):"
