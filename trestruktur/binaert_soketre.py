from trestruktur import student as std

class Node:
    def __init__(self, nokkel, verdi, forelder=None):
        self.nokkel = nokkel
        self.verdi = verdi
        self.forelder = forelder
        self.venstre_barn = None
        self.hoyre_barn = None

    def rekursiv_preorder_utskrift(self, nivaa=0):
        for i in range(nivaa):
            print("\t", end="")
        print(f"({self.nokkel}, {self.verdi})")
        if self.venstre_barn is not None:
            self.venstre_barn.rekursiv_preorder_utskrift(nivaa+1)
        if self.hoyre_barn is not None:
            self.hoyre_barn.rekursiv_preorder_utskrift(nivaa+1)

    def er_bladnode(self):
        if self.venstre_barn is None and self.hoyre_barn is None:
            return True
        return False


class BinaertSoketre:
    def __init__(self):
        self.rot = None

    def skriv_treemap(self):
        self.rot.rekursiv_preorder_utskrift()

    # Setter inn en oppgitt nøkkel med oppgitt verdi, overskriver gammel verdi
    # hvis nøkkelen allerede ligger der
    #
    # Kjøretid O(høyden til treet)
    def put(self, nokkel, verdi):
        if self.rot is None:
            self.rot = Node(nokkel, verdi)
        else:
            nv_node = self.rot
            ferdig = False
            while not ferdig:
                if nokkel < nv_node.nokkel:
                    if nv_node.venstre_barn is None:
                        nv_node.venstre_barn = Node(nokkel, verdi, nv_node)
                        ferdig = True
                    else:
                        nv_node = nv_node.venstre_barn
                elif nokkel == nv_node.nokkel:
                    nv_node.verdi = verdi
                    ferdig = True
                else:
                    if nv_node.hoyre_barn is None:
                        nv_node.hoyre_barn = Node(nokkel, verdi, nv_node)
                        ferdig = True
                    else:
                        nv_node = nv_node.hoyre_barn

    def __setitem__(self, key, value):
        self.put(key, value)

    # Kjøretid O(høyden til treet)
    def finn_node(self, nokkel):
        if self.rot is None:
            return None
        nv_node = self.rot
        ferdig = False
        while not ferdig:
            if nokkel == nv_node.nokkel:
                ferdig = True
                return nv_node
            if nokkel < nv_node.nokkel:
                if nv_node.venstre_barn is None:
                    return None
                else:
                    nv_node = nv_node.venstre_barn
            else:       # nokkel > nv_node.nokkel
                if nv_node.hoyre_barn is None:
                    return None
                else:
                    nv_node = nv_node.hoyre_barn

    # Henter ut verdien for oppgitt nøkkel
    #
    # Kjøretid O(høyden til treet)
    def get(self, nokkel):
        noden = self.finn_node(nokkel)
        if noden is None:
            raise KeyError(f"Finner ikke nøkkelen {nokkel}")
        return noden.verdi

    def __getitem__(self, key):
        return self.get(key)

    # Fjerner en nøkkel fra map-et. Fjerner også verdien.
    #
    # Finn node: O(høyden til treet)
    def delete(self, nokkel):
        if self.rot is None:
            return
        noden = self.finn_node(nokkel)
        if noden.er_bladnode():
            if noden.forelder is None:
                self.rot = None
            elif noden.forelder.venstre_barn == noden:      # Er denne noden venstre barnet til forelderen
                noden.forelder.venstre_barn = None
            else:
                noden.forelder.hoyre_barn = None
            noden.forelder = None
        elif noden.venstre_barn is not None and noden.hoyre_barn is None:
            if noden.forelder is None:
                self.rot = noden.venstre_barn
            elif noden.forelder.venstre_barn == noden:
                noden.forelder.venstre_barn = noden.venstre_barn
            else:
                noden.forelder.hoyre_barn = noden.venstre_barn
            noden.venstre_barn.forelder = noden.forelder
            noden.forelder = None
        elif noden.venstre_barn is None and noden.hoyre_barn is not None:
            if noden.forelder is None:
                self.rot = noden.hoyre_barn
            elif noden.forelder.venstre_barn == noden:
                noden.forelder.venstre_barn = noden.hoyre_barn
            else:
                noden.forelder.hoyre_barn = noden.hoyre_barn
            noden.hoyre_barn.forelder = noden.forelder
            noden.forelder = None
        else:
            ny_node = self.finn_hoyeste_barn(noden.venstre_barn)
            self.delete(ny_node.nokkel)
            noden.nokkel = ny_node.nokkel
            noden.verdi = ny_node.verdi

    def finn_hoyeste_barn(self, node):
        nv_node = node
        while nv_node.hoyre_barn is not None:
            nv_node = nv_node.hoyre_barn
        return nv_node

    # Finnes nøkkelen i samlingen?
    #
    # Kjøretid O(høyden til treet)
    def contains(self, nokkel):
        noden = self.finn_node(nokkel)
        if noden is None:
            return False
        return True

    def __contains__(self, nokkel):
        return self.contains(nokkel)

    # Hent første nøkkel som er større enn oppgitt nøkkel hvis det fins en slik
    #
    # Kjøretid O(høyden til treet)
    def next(self, nokkel):
        if self.rot is None:
            return None
        nv_node = self.rot
        ferdig = False
        verdi = None
        while not ferdig:
            if nokkel < nv_node.nokkel:
                verdi = nv_node.nokkel
                if nv_node.venstre_barn is None:
                    return verdi
                else:
                    nv_node = nv_node.venstre_barn
            if nokkel >= nv_node.nokkel:
                if nv_node.hoyre_barn is None:
                    return verdi
                else:
                    nv_node = nv_node.hoyre_barn

    # Hent ut første nøkkel som er mindre
    #
    # Kjøretid O(høyden til treet)
    def previous(self, nokkel):
        if self.rot is None:
            return None
        nv_node = self.rot
        ferdig = False
        verdi = None
        while not ferdig:
            if nokkel > nv_node.nokkel:
                verdi = nv_node.nokkel
                if nv_node.hoyre_barn is None:
                    return verdi
                else:
                    nv_node = nv_node.hoyre_barn
            if nokkel <= nv_node.nokkel:
                if nv_node.venstre_barn is None:
                    return verdi
                else:
                    nv_node = nv_node.venstre_barn

    # Hent ut den laveste nøkkelen
    #
    # Kjøretid O(høyden til treet)
    def first(self):
        nv_node = self.rot
        while nv_node.venstre_barn is not None:
            nv_node = nv_node.venstre_barn
        return nv_node.nokkel

    # Hent ut den høyeste nøkkelen
    #
    # Kjøretid O(høyden til treet)
    def last(self):
        nv_node = self.finn_hoyeste_barn(self.rot)
        return nv_node.nokkel

    # Hent ut alle nøkler mellom to oppgitte nøkler
    def between(self, forste, siste):
        if self.rot is None:
            return None
        nv_node = self.rot
        ferdig = False
        node = None
        while not ferdig:
            if forste < nv_node.nokkel:
                node = nv_node
                if nv_node.venstre_barn is None:
                    break
                else:
                    nv_node = nv_node.venstre_barn
            if forste >= nv_node.nokkel:
                if nv_node.hoyre_barn is None:
                    break
                else:
                    nv_node = nv_node.hoyre_barn
        resultater = []
        iterator = BinaertSoketreIterator(self, node)
        nokkel = node.nokkel
        try:
            while nokkel < siste:
                nokkel = iterator.__next__()
                if nokkel >= siste:
                    break
                resultater.append(nokkel)
        except StopIteration:
            pass
        return resultater


    # Finn det k-ende elementet, Selection problemet
    #
    # Starte iteratoren: O(høyden til treet)
    # Gå k hakk: O(k*høyden til treet)
    def finn_k_ende(self, k):
        iterator = self.__iter__()
        nokkel = None
        try:
            for i in range(k):
                nokkel = iterator.__next__()
        except StopIteration:
            return None
        return nokkel

    def __iter__(self):
        return BinaertSoketreIterator(self)


class BinaertSoketreIterator:
    def __init__(self, treet, startnode=None):
        if startnode is None:
            self.nv_node = treet.rot
            while self.nv_node.venstre_barn is not None:
                self.nv_node = self.nv_node.venstre_barn
        else:
            self.nv_node = startnode

    def __next__(self):
        if self.nv_node is None:
            raise StopIteration
        nokkelen = self.nv_node.nokkel
        if self.nv_node.hoyre_barn is not None:
            self.nv_node = self.nv_node.hoyre_barn
            while self.nv_node.venstre_barn is not None:
                self.nv_node = self.nv_node.venstre_barn
        else:
            while self.nv_node.forelder is not None and self.nv_node == self.nv_node.forelder.hoyre_barn:
                self.nv_node = self.nv_node.forelder
            if self.nv_node.forelder is None:
                self.nv_node = None
            else:
                self.nv_node = self.nv_node.forelder
        return nokkelen

    def __iter__(self):
        return self


if __name__ == "__main__":
    studentliste = std.lag_student_liste()
    map = BinaertSoketre()
    for student in studentliste:
        map.put(student.get_etternavn(), student)
    print()
    for student in map:
        print(student)
    map.skriv_treemap()
    print()
    print(map.get("Vik"))
    print(map.get("Nilsen"))
    print()
    print(map.contains("Herrem"))
    print(map.contains("Tøssebro"))
    print()
    print(map.next("E"))
    print(map.previous("E"))
    print()
    print(map.finn_k_ende(3))
    print()
    print(map.between("F", "O"))
    map.delete("Nilsen")
    map.skriv_treemap()
    for student in map:
        print(student)
    print()
    print(map.get("Ytrebø"))
    print(map.get("Hansen"))
    print()
    map.delete("Hansen")
    map.skriv_treemap()
    for student in map:
        print(student)
    print()
    print(map.get("Ytrebø"))
    print(map.get("Erlingsen"))
    print()