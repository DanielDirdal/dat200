from lister.stabel_liste import Stabel

# Må sjekke for kommentarer
def parentessjekker(filnavn):
    stabel = Stabel()
    linjenummer = 0
    with open(filnavn, "r") as fila:
        for linje in fila:
            linjenummer += 1
            for tegn in linje:
                if tegn == "(":
                    stabel.push("(")
                if tegn == "[":
                    stabel.push("[")
                if tegn == "{":
                    stabel.push("{")
                if tegn == ")":
                    siste_parantes = stabel.pop()
                    if siste_parantes != "(":
                        print(f"Feil parantes i linje {linjenummer}, forventet ( men fant {siste_parantes}")
                        return
                if tegn == "]":
                    siste_parantes = stabel.pop()
                    if siste_parantes != "[":
                        print(f"Feil parantes i linje {linjenummer}, forventet [ men fant {siste_parantes}")
                        return
                if tegn == "}":
                    siste_parantes = stabel.pop()
                    if siste_parantes != "{":
                        print(f"Feil parantes i linje {linjenummer}, forventet krøøparentes men fant {siste_parantes}")
                        return

    if not stabel.is_empty():
        print("Mangler match for følgende parenteser: ")
        while not stabel.is_empty():
            print(stabel.pop())
    else:
        print(f"Sjekk er OK. Sjekket {linjenummer} linjer")


if __name__ == "__main__":
    filnavn = input("Filnavn: ")
    parentessjekker(filnavn)
