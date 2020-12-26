# Enkel splitt og hersk algoritme
def finn_hoyeste_element_spitt_og_hersk(liste):
    if len(liste) == 1:
        return liste[0]
    if len(liste) == 2:
        if liste[1] > liste[0]:
            return liste[1]
        else:
            return liste[0]
    hoyeste_1 = finn_hoyeste_element_spitt_og_hersk(liste[:len(liste)//2])
    hoyeste_2 = finn_hoyeste_element_spitt_og_hersk(liste[len(liste)//2:])
    if hoyeste_1 > hoyeste_2:
        return hoyeste_1
    else:
        return hoyeste_2

if __name__ == "__main__":
    liste = [8, 2, 7, 3, 16, 78, 3, 6, 3, 3, 7, 95, 4, 3]
    print(finn_hoyeste_element_spitt_og_hersk(liste))