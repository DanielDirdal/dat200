import numpy as np

class ArrayListe:
    def __init__(self, startkapasitet=10):
        self.array = np.zeros(startkapasitet, dtype=object)
        self.lengde = 0
        self.start = 3

    # gir resultatet av len funksjonen
    def __len__(self):
        return self.lengde

    # Kjøretid Theta(n)
    def utvid(self, ny_storrelse=None):
        if ny_storrelse is None:
            ny_storrelse = len(self.array)*2
        ny_array = np.zeros(ny_storrelse, dtype=object)
        for index in range(len(self.array)):
            ny_array[index] = self.array[index]
        self.array = ny_array

    # Kjøretid Theta(n)
    def utvidleft(self, ny_storrelse=None):
        if ny_storrelse is None:
            ny_storrelse = len(self.array)*2
        ny_array = np.zeros(ny_storrelse, dtype=object)
        start = len(self.array)
        lengde = self.array - self.start
        for index in range(len(lengde)):
            ny_array[index + start] = self.array[index + self.start]
        self.array = ny_array
        self.start = start


    # Legger inn det oppgitte elementet på oppgitt indeks, og forskyver alle elementer som ligger
    # etterpå ett hakk bak
    # Kjøretid O(n)
    def insert(self, indeks, element):
        if self.lengde + self.start >= len(self.array):
            self.utvid()
        for index in range(self.lengde+self.start-1, indeks+self.start-1, -1):
            self.array[index+1] = self.array[index]
        self.array[indeks+self.start] = element
        self.lengde += 1

    # Returnerer elementet på oppgitt indeks.
    # Tilsvarer Python variabel = liste[indeks]
    # Kjøretid Theta(1)
    def get(self, indeks):
        return self.array[indeks+self.start]


    # Legger et element på slutten av køen. Tilsvarer enqueue
    # Kjøretid: Theta(n) worst case
    #           Theta(1) best case
    def append(self, element):
        if self.lengde + self.start >= len(self.array):
            self.utvid()
        self.array[self.lengde+self.start] = element
        self.lengde += 1

    # Legger et element på starten av køen
    # Kjøretid: Theta(n) worst case
    #           Theta(1) best case
    def appendleft(self, element):
        if self.start <= 0:
            self.utvidleft()
        self.array[self.start-1] = element
        self.lengde += 1
        self.start -= 1

    # Tar ut et element fra slutten av køen
    # Kjøretid Theta(1)
    def pop(self):
        verdi = self.array[self.lengde+self.start-1]
        self.array[self.lengde+self.start-1] = 0
        self.lengde -= 1
        return verdi

    # Tar ut et element fra starten av køen. Tilsvarer dequeue
    # Kjøretid Theta(1)
    def popleft(self):
        verdi = self.array[self.start]
        self.array[self.start] = 0
        self.start += 1
        self.lengde -= 1
        return verdi

    # Gå gjennom lista, element for element
    def __iter__(self):
        return ArrayListIterator(self)

class ArrayListIterator:
    def __init__(self, lista):
        self.lista = lista
        self.nv_element = 0

    def __next__(self):
        if self.nv_element >= len(self.lista):
            raise StopIteration
        resultat = self.lista.get(self.nv_element)
        self.nv_element += 1
        return resultat

if __name__ == "__main__":
    arrayliste = ArrayListe()
    arrayliste.append(1)
    arrayliste.append(2)
    print(arrayliste.array)
    print()
    arrayliste.insert(0, 3)
    print(arrayliste.array)
    print()
    arrayliste.appendleft(5)
    arrayliste.appendleft(6)
    arrayliste.appendleft(7)
    print()
    print(arrayliste.array)
    print(arrayliste.lengde)
    print()
    arrayliste.insert(0, 8)
    arrayliste.append(1)
    arrayliste.append(2)
    arrayliste.append(3)
    arrayliste.insert(0, 9)
    print()
    print(arrayliste.array)
    print(arrayliste.lengde)
    print()
    arrayliste.append(3)
    arrayliste.append(4)
    arrayliste.append(5)
    arrayliste.append(6)
    print()
    print(arrayliste.array)
    print(arrayliste.lengde)
    arrayliste.insert(0, 9)
    print()
    print(arrayliste.array)
    print(arrayliste.lengde)
    print()
    print(arrayliste.get(10))
    arrayliste.append(7)
    print(arrayliste.get(11))
    print(arrayliste.get(12))
    arrayliste.append(8)
    arrayliste.appendleft(10)
    print()
    print()
    print(arrayliste.array)
    print(arrayliste.lengde)
    print()
    print(arrayliste.pop())
    print(arrayliste.popleft())
    print()
    print(arrayliste.array)
    print(arrayliste.lengde)
    arrayliste.appendleft(4)
    arrayliste.appendleft(4)
    arrayliste.appendleft(4)
    arrayliste.appendleft(4)
    arrayliste.appendleft(4)
    arrayliste.appendleft(4)
    arrayliste.appendleft(4)
    arrayliste.appendleft(4)
    arrayliste.appendleft(4)
    arrayliste.appendleft(4)
    print()
    print(arrayliste.array)
