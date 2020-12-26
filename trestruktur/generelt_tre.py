# Array-liste basert tre, array-liste av barn i hver node!
class Tre:
    def __init__(self, dataobjekt):
        self.data = dataobjekt
        self.barn = []              # Liste av tre-objekter
        self.forelder = None

    # Kjøretid Theta(1)
    def legg_til_barn(self, undertre):      # Undertre skal v're av typen tre
        self.barn.append(undertre)
        undertre.forelder = self
