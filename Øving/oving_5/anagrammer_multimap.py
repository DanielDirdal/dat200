def beregn_representant(ord):
    bokstavliste = []
    for bokstav in ord:
        bokstavliste.append(bokstav)
    bokstavliste.sort()
    representant = ""
    for bokstav in bokstavliste:
        representant = representant + bokstav
    return representant


# Multimap: Python dictionary hvor hvert element er ei liste heller enn et enkelt element
def lag_anagram_dictionary(ordliste):
    anagram_dictionary = {}
    for ord in ordliste:
        representant = beregn_representant(ord)
        if representant in anagram_dictionary:      # Hvis representanten allerede er med i dictionariet, legg inn ordet i lista
            anagram_dictionary[representant].add(ord)
        else:                                       # Ellers legg inn ei ny liste med ordet i dictionariet
            mengde = set()
            mengde.add(ord)
            anagram_dictionary[representant] = mengde
    return anagram_dictionary


def finn_anagram(ord, anagram_dictionary):
    representant = beregn_representant(ord)
    anagram = anagram_dictionary[representant]
    return anagram


if __name__ == "__main__":
#    ordliste = ["mot", "opp", "ned", "tom", "den", "rar", "tar", "var", "art", "rav", "arv"]
    ordliste = []
    with open("ordfil_for_anagrammer.txt") as ordfil:
        for linje in ordfil:
            ordene = linje.split()
            for ord in ordene:
                ordliste.append(ord)
    anagram_dictionary = lag_anagram_dictionary(ordliste)
    anagram = finn_anagram("arv", anagram_dictionary)
    print(anagram)
