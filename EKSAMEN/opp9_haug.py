from prioritetskoer.binaerhaug import Prioritetsko
class Intervall:
    def __init__(self, start, slutt):
        if slutt < start:
            raise ValueError("Et intervall kan ikke slutte før det starter!")
        self.__start = start
        self.__slutt = slutt
    @property
    def start(self):
        return self.__start
    @property
    def slutt(self):
        return self.__slutt
    def __str__(self):
        return f"Intervall ({self.start} -> {self.slutt})"

# Forventer ei liste av intervaller som input
def intervall_tester(intervall_liste):
    koe = Prioritetsko()                        # Binærhaug / Binary Heap
    resultat = []
    aktive = []
    for intervall in intervall_liste:
        koe.add(intervall, intervall.start)
    while len(koe) > 0:
        nv_tid = koe.lavest_prioritet()         # Henter ut prioriteten til elementet som skal hentes ut. Kjøretid Theta(1)
        nv_intervall = koe.remove()
        if nv_tid == nv_intervall.start:
            koe.add(nv_intervall, nv_intervall.slutt)
            for intervall in aktive:
                resultat.append((nv_intervall, intervall))
            aktive.append(nv_intervall)
        else:
            aktive.remove(nv_intervall)
    return resultat