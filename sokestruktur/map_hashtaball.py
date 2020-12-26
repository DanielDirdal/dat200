import numpy as np
from sokestruktur import student as std

class HashMap:
    # Konstruktør: Theta(n)
    def __init__(self, startkapasitet=20):
        self.array = np.zeros(startkapasitet, dtype=object)
        self.antall_elementer = 0

    def rehash(self):
        ny_array = np.zeroes(len(self.array)*2, dtype=object)
        for element in self:
            self.put(element, self[element], ny_array)
        self.array = ny_array

    # Kjøretid: Theta(1)
    def finn_hashverdi(self, nokkel, array=None):
        if array is None:
            array = self.array
        hashverdi = hash(nokkel)
        if hashverdi < 0:
            hashverdi = -hashverdi
        hashverdi = hashverdi % len(array)
        return hashverdi


    # Setter inn en oppgit nøkkel med oppgit verdi, overskriver gammel verdi
    # hvis nøkkelen allerede ligger der
    #
    # Kjøretid: Theta(1) uten prøving
    # Med prøving, kjøretid O(antall forsøk)
    def put(self, nokkel, verdi, array=None):
        ok_antall_elementer = False
        if array is None:
            array = self.array
            ok_antall_elementer = True
        if (self.antall_elementer + 1)/len(array) > 0.7:
            self.rehash()
        liste_element = (nokkel, verdi)
        hashverdi = self.finn_hashverdi(nokkel, array)
        while array[hashverdi] != 0 and array[hashverdi][0] != nokkel and array[hashverdi][0] is not None:
            hashverdi += 1
            hashverdi = hashverdi % len(array)
        if array[hashverdi] == 0:
            array[hashverdi] = liste_element
            if ok_antall_elementer:
                self.antall_elementer += 1
        elif array[hashverdi][0] == nokkel:
            array[hashverdi] = liste_element
        elif array[hashverdi][0] is None:
            array[hashverdi] = liste_element
            if ok_antall_elementer:
                self.antall_elementer += 1


    def __setitem__(self, key, value):
        self.put(key, value)

    # Henter ut verdien for oppgitt nøkkel
    #
    # Kjøretid: Theta(1)
    def get(self, nokkel):
        hashverdi = self.finn_hashverdi(nokkel)
        while self.array[hashverdi] != 0 and self.array[hashverdi][0] != nokkel or self.array[hashverdi][0] is None:
            hashverdi += 1
            hashverdi = hashverdi % len(self.array)
        if self.array[hashverdi] == 0:
            raise KeyError(f"Finner ikke nøkkelen {nokkel}")
        return self.array[hashverdi][1]

    def __getitem__(self, key):
        return self.get(key)

    # Fjerne en nøkkel fra map-et. Fjener også verdien.
    #
    # Kjøretid: Theta(1)
    def delete(self, nokkel):
        hashverdi = self.finn_hashverdi(nokkel)
        while self.array[hashverdi] != 0 and self.array[hashverdi][0] != nokkel or self.array[hashverdi][0] is None:
            hashverdi += 1
            hashverdi = hashverdi % len(self.array)
        if self.array[hashverdi] != 0 and self.array[hashverdi][0] == nokkel:
            self.array[hashverdi] = (None, None)
            self.antall_elementer -= 1

    # Finnes nøkkelen i samlingen
    #
    # Kjøretid: Theta(1)
    def contains(self, nokkel):
        hashverdi = self.finn_hashverdi(nokkel)
        while self.array[hashverdi] != 0 and self.array[hashverdi][0] != nokkel or self.array[hashverdi][0] is None:
            hashverdi += 1
            hashverdi = hashverdi % len(self.array)
        if self.array[hashverdi] != 0 and self.array[hashverdi][0] == nokkel:
            return True
        return False

    def __contains__(self, nokkel):
        return self.contains(nokkel)

    def __len__(self):
        return self.antall_elementer

    # Iterator: Trenger en iterator som returnere nøkler slik at man kan bruke
    # en for-loop til å gå gjennom alle nøklene i samlingen.
    #
    # Kjøretid hele iterasjonen: Theta(lengden til lista)
    def __iter__(self):
        return HashMapiterator(self)

class HashMapiterator:
    def __init__(self, hashmapet):
        self.hashmapet = hashmapet
        self.index = 0

    def __next__(self):
        while self.index < len(self.hashmapet.array) and self.hashmapet.array[self.index] == 0:
            self.index += 1
        if self.index >= len(self.hashmapet.array):
            raise StopIteration
        nokkel = self.hashmapet.array[self.index][0]
        self.index += 1
        return nokkel

    def __iter__(self):
        return self

if __name__ == "__main__":
    studentliste = std.lag_student_liste()
    map = HashMap()
    for student in studentliste:
        map.put(student.get_etternavn(), student)
    for nokkel in map:
        print(f"{nokkel}: {map[nokkel]}")
    print()
    print(map.get("Vik"))
    print(map.get("Nilsen"))
    print()
    map.delete("Vik")
    for nokkel in map:
        print(f"{nokkel}: {map[nokkel]}")