
def legger_ord_i_dic(filnavn):
    map = dict()
    try:
        with open(filnavn, "r") as fil:
            linje = fil.readline()
            for linje in fil:
                liste_linje = linje.split()
                for ord in liste_linje:
                    ordet = sorted(ord)
                    ordet = ''.join(ordet)
                    map[ord] = ordet
    except IOError as e:
        print("Feil i håndtering av fil: " + str(e))
    except UnicodeDecodeError as e:
        print("Feil i koding av tekstil: " + str(e))
    except ValueError as e:
        print("Feil i tall håndtering: " + str(e))
    return map

def sjekk_anagrammer(dic, ord):
    lista = []
    teller = 0
    for i in dic:
        if dic[i] == dic[ord] and i != ord:
            lista.append(i)
            teller += 1
    return lista, teller


if __name__ == "__main__":
    filnavn = "ordfil_for_anagrammer.txt"
    map = legger_ord_i_dic(filnavn)
    print(map)
    for i in map:
        print(f"key: {i} gir verdi {map[i]}")
    ord = input("Hva ord vil du sjekke: ")
    liste, antall = sjekk_anagrammer(map, ord)
    print(f"Antall ord som er anagrammer er: {antall}")
    print(f" Disse ordene er angrammer av {ord}")
    print(liste)