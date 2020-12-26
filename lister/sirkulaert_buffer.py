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
        self.__neste %= len(self.__liste) # if self.__neste >= len(self.__liste): self.__neste = 0


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


class Deque:
    # Legger et element på slutten av køen. Tilsvarer enqueue
    def append(self, element):
        pass

    # Legger et element på starten av køen
    def appendleft(self, element):
        pass

    # Tar ut et element fra slutten av køen
    def pop(self):
        pass

    # Tar ut et element fra starten av køen. Tilsvarer dequeue
    def popleft(self):
        pass

    # Returnerer siste element i køen uten å fjerne det
    def peek(self):
        pass

    # Returnerer første element i køen uten å fjerne det
    def peekleft(self):
        pass

if __name__ == "__main__":
    buffer = Koe(5)
    buffer.enqueue(1)
    buffer.enqueue(2)
    buffer.enqueue(3)
    print(buffer.dequeue())
    print(buffer.dequeue())
    buffer.enqueue(4)
    buffer.enqueue(5)
    buffer.enqueue(6)
    buffer.enqueue(7)
    print(buffer.dequeue())
    print(buffer.dequeue())
    print(buffer.dequeue())
    print(buffer.dequeue())