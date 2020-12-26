# Eksempel på algoritmeanalyse: Finn element i liste

# problem: Gitt ei liste og et element, finn første indeks i lista som inneholder dette elementet
# rerturner -1 hvis lista ikke inneholder dette elementer.
#
# Første indeks siden lister kan inneholde duplikater

# Enkel algoritme: Gå gjennom lista fra starten, element for element, og sjekk om dette element er like det du leiter etter
# Sekvensielt søk

# Analyse:
# Worst case: n ganger, elementet er siste element eller ikke i liste, O(n)
# Best case: 1 gang, elementer er først i lista, O(1)
# Gjennomsnittlig tilfelle: O(n)
def finn_element(element, liste):
    for index in range(len(liste)):         # Kjører maks n ganger
        if element == liste[index]:         # Kjører maks n ganger
            return index                    # Kjører maks 1 gang
    return -1                               # Kjører maks 1 gang

# Eksempel
liste = [8, 2, 5, 3, 15, 4, 5, 13, 76, 53]
element = 4
print(finn_element(element, liste))