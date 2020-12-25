import numpy as np

class Koe:
    def __init__(self, kapasitet):
        self.__liste = np.zeros(kapasitet, dtype=object)
        self.__neste = 0
        self.__forste = 0
        self.__lengde = 0

    # Legger et element på slutten av køen
    def enqueue(self, element):
        if self.__lengde >= len(self.__liste):
            raise ValueError("Bufferet er fullt")
        self.__liste[self.__neste] = element
        self.__neste += 1
        self.__lengde += 1
        self.__neste %= len(self.__liste)  # if self.__neste >= len(self.__liste): self.__neste = 0

    # Tar ut et element fra starten av køen
    def dequeue(self):
        if self.__lengde <= 0:
            raise ValueError("Bufferet er tomt")
        verdi = self.__liste[self.__forste]
        self.__forste += 1
        self.__lengde -= 1
        self.__forste %= len(self.__liste)
        return verdi

    # Returnerer første element i køen uten å fjerne det
    def peek(self):
        if self.__lengde <= 0:
            raise ValueError("Bufferet er tomt")
        return self.__liste[self.__forste]

    def get(self, i):
        if self.__lengde <= 0:
            raise ValueError("Bufferet er tomt")
        if i > self.__lengde:
            raise ValueError("Indekse verdien er utforbi bufferet")
        return self.__liste[i]

    def as_list(self):
        liste = []
        if self.__lengde <= 0:
            raise ValueError("Bufferet er tomt")
        for i in range(self.__lengde):
            liste.append(self.get(i))
        return liste

    def __len__(self):
        return self.__lengde

if __name__ == "__main__":
    koe = Koe(5)
    koe.enqueue(2)
    koe.enqueue(3)
    koe.enqueue(4)
    koe.enqueue(5)
    print(koe.get(3))
    liste = koe.as_list()
    print(liste)