# Fordel: Effektiv lagring, trenger ikke et liste_objket for hver node
# Ulempe: Tregere innsetting og navigering
# I praksis ei lenket liste av barn i stedet for ei array-liste.
class Tre:
    def __init__(self, dataobjeket):
        self.data = dataobjeket
        self.forelder = None
        self.forste_barn = None
        self.sosken = None

    # Kjøretid Theta(antall barn)
    def legg_til_bar(self, undertre):
        undertre.forelder = self
        if self.forste_barn is None:
            self.forste_barn = undertre
        else:
            nv_barn = self.forste_barn
            while nv_barn.sosken is not None:
                nv_barn = nv_barn.sosken
            nv_barn.sosken = undertre

