class Stabel:
    def __init__(self):
        self.__liste = []

    # Legget et nytt element på stabelen
    # Kjøretid O(1)
    def push(self, element):
        self.__liste.append(element)

    # Tar av et element fra stabelen og returnerer det
    # Kjøretid O(1)
    def pop(self):
        element = self.__liste[-1]
        del self.__liste[-1]
        return element

    # Returnere overste element uten å fjerne det
    # Kjøretid O(1)
    def peek(self):
        element = self.__liste[-1]
        return element

    # Kjøretid O(1)
    def is_empty(self):
        if len(self.__liste) == 0:
            return True
        return False