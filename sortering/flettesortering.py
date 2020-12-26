import sortering.innsettingssortering

# Kombiner sorterte lister ( l1, l2 )
# Lag referanser r1 og r2 som begge er indeksier inn i sin respektive lister og som begge starter på 0
# Frotsett til enten r1 eller r2 er forbi slutten på lista si
#       Sammenlikn l1(r1) og l2(r2)
#           Hvis l1(r1) <= l2(r2): Sett inn l1(r1) i resultatet og øk r1 med 1
#           Ellers sett inn r2(l2) og øk r2 med 1
# Legg inn det som mangler fra den lista som ikke ble ferdig
#
# Kjøretid: Går gjennom begge listene eksat 1 gang, Theta(m + n)
# Minnebruk: Theta(m + n)
def kombiner_sorterte_lister(liste1, liste2):
    index1 = 0
    index2 = 0
    resultat = []
    while index1 < len(liste1) and index2 < len(liste2):
        if liste1[index1] <= liste2[index2]:
            resultat.append(liste1[index1])
            index1 += 1
        else:
            resultat.append(liste2[index2])
            index2 += 1
    while index1 < len(liste1):
        resultat.append(liste1[index1])
        index1 += 1
    while index2 < len(liste2):
        resultat.append(liste2[index2])
        index2 += 1
    return resultat

# Splitt og hersk sortering med fletting
# Basetilfelle: lista har ett element: Da er den sortert og den skal selv returneres
# Basetilfelle, to elementer: Hvis de er io feil rekkefølge, bytt dem om
# Ellers, kall meg selv med første halvpart, kall meg selv med andre halvpart, kombiner de to
#
# Rekurrensliking T(n) = Theta(n) + 2*t(n/2)
# Kjøretid: Theta(n*log(n))
# Minnebruk: Theta(n*log(n))
def flettesortering(liste):
    if len(liste) <= 1:                                     # Theta(1)
        return liste
    if len(liste) == 2:                                     # Theta(1)
        if liste[0] > liste[1]:
            temp = liste[0]
            liste[0] = liste[1]
            liste[1] = temp
        return liste
    forste = flettesortering(liste[0:len(liste)//2])        # Theta(n)
    andre = flettesortering(liste[len(liste)//2:])          # Theta(n)
    return kombiner_sorterte_lister(forste, andre)          # Theta(n)


def flettesortering_bytter_algoritme(liste):
    if len(liste) <= 10:                                     # Theta(1)
        sortering.innsettingssortering.sorter(liste)
        return liste
    forste = flettesortering(liste[0:len(liste)//2])        # Theta(n)
    andre = flettesortering(liste[len(liste)//2:])          # Theta(n)
    return kombiner_sorterte_lister(forste, andre)          # Theta(n)



if __name__ == "__main__":
    liste = [1, 6, 8, 11, 15]
    liste2 = [-5, -2, 7, 8, 12, 17, 25]
    print(kombiner_sorterte_lister(liste, liste2))
    liste = [7, 3, 5, 4, 8, 2, -4, -5, 4]
    print(liste)
    liste_sortert = flettesortering(liste)
    print(liste_sortert)