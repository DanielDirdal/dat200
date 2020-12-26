# Problemstørrelse n er her lengden til lista
# Kjøretid: O(n**2)
# Plassbruk O(1)
def maksimum(lista):
    for index in range(len(lista)):         # Kjører n ganger
        element = lista[index]              # Kjører n ganger
        for j in range(len(lista)):         # Kjører n*n ganger
            if element < lista[j]:          # Kjører n*n ganger
                break
        if element < lista[j]:              # Kjører n ganger
            continue
        else:
            return element                  # Kjører 1 gang


# Kjøretid: O(n)
# Kjøretid: O(1)
def maksimum2(lista):
    maks_hittil = lista[0]                  # Kjører 1 gang, Å hente ut et element går i konstand tid
    for element in lista:                   # Kjører n ganger
        if element > maks_hittil:           # Kjører n ganger
            maks_hittil = element           # Kjører 0 beste tilfelle -  første element høyest,
                                            # Kjører n ganger i verste tilfelle - lista er sortert stigende
    return maks_hittil                      # Kjører 1 gang


liste = [-6, 5, 2, 8, -4, 12, 5, 21, 3]
print(maksimum(liste))
print(maksimum2(liste))
