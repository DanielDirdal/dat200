class Hanoi:
    def __init__(self, navn, posisjon):
        self.navn = navn
        self.posisjon = posisjon

    @property
    def posisjon(self):
        return self.__posisjon

    @posisjon.setter
    def posisjon(self, ny_posisjon):
        self.__posisjon = ny_posisjon

    def __str__(self):
        return f"Disk {self.navn} er på posisjon {self.posisjon}"


# Kjøretid er O(2^n) på grunn av at kver funksjon kalle på seg selv to ganger
def hanoi_tower(n, start, mellomledd, slutt, liste):
    if n == 1:
        print("Move disk 1 from rod " + start, "to rod " + slutt)
        liste[n-1].posisjon = slutt
        for j in range(len(liste)):
            print(liste[j])
        return
    else:
        hanoi_tower(n - 1, start, slutt, mellomledd, liste)
        print("Move disk", n, "from rod", start, "to rod", slutt)
        liste[n - 1].posisjon = slutt
        for j in range(len(liste)):
            print(liste[j])
        hanoi_tower(n - 1, mellomledd, start, slutt, liste)


if __name__ == "__main__":
    n = 3
    liste = []
    for i in range(1, n + 1, 1):
        test = Hanoi(i, "A")
        liste.append(test)
    hanoi_tower(n, "A", "B", "C", liste)