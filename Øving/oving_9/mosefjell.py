from grafer.dijkstra import *
from grafer.graf_nabolister import *

def les_kartfil(filnavn):
    try:
        with open(filnavn, "r") as fil:
            bredde = int(fil.readline())
            hoyde = int(fil.readline())
            start_x = int(fil.readline())
            start_y = int(fil.readline())
            slutt_x = int(fil.readline())
            slutt_y = int(fil.readline())
            rader = []
            for i in range(hoyde):
                rader.append([])
                linje = fil.readline()
                punkter = linje.split(",")
                for punkt in punkter:
                    verdi = int(punkt)
                    rader[i].append(verdi)
            return bredde, hoyde, start_x, start_y, slutt_x, slutt_y, rader
    except IOError as e:
        print("Feil i håndtering av fil: " + str(e))
    except UnicodeDecodeError as e:
        print("Feil i koding av tekstil: " + str(e))
    except ValueError as e:
        print("Feil i tall håndtering: " + str(e))

def nodeindeks_utregning(x, y, bredde):
    return y*bredde + x

def lag_graf(bredde, hoyde, rader):
    grafen = GrafNaboliste()
    for i in range(hoyde):
        for j in range(bredde):
            grafen.add_node(f"({j},{i})")
    teller = 0
    for i in range(hoyde):
        for j in range(bredde):
            grafen.set_kostnad(teller, rader[i][j])
            teller += 1
    for y in range(hoyde-1):
        for x in range(bredde):
            node_indeks = nodeindeks_utregning(x, y, bredde)
            vertikal_nabo_indeks = nodeindeks_utregning(x, y+1, bredde)
            grafen.add_edge(node_indeks, vertikal_nabo_indeks, abs(rader[y][x] - rader[y+1][x]) + 1)
            grafen.add_edge(vertikal_nabo_indeks, node_indeks, abs(rader[y][x] - rader[y+1][x]) + 1)
            if x < bredde-1:
                horisontal_nabo_indeks = nodeindeks_utregning(x+1, y, bredde)
                grafen.add_edge(node_indeks, horisontal_nabo_indeks, abs(rader[y][x] - rader[y][x+1]) + 1)
                grafen.add_edge(horisontal_nabo_indeks, node_indeks, abs(rader[y][x] - rader[y][x + 1]) + 1)
    return grafen


if __name__ == "__main__":
    filnavn = "oving_9_eksempelfil.txt"
    bredde, hoyde, start_x, start_y, slutt_x, slutt_y, rader = les_kartfil(filnavn)
    grafen = lag_graf(bredde, hoyde, rader)
    print("Bredde: " + str(bredde))
    print("Høyde: " + str(hoyde))
    print(f"Startposisjon: ({start_x}, {start_y})")
    print(f"Sluttposisjon: ({slutt_x}, {slutt_y})")
    for rad in rader:
        for kolonne in rad:
            print(f" {kolonne:2d}", end="")
        print()
    print()
    dijkstra(grafen, 49, 58)
    print(f"Korteste vei fra (1,4) til (10,4) : {grafen.get_kostnad(58)}")
    skriv_utkorteste_vei(grafen, 58)
    print()
    print(grafen.get_vekt(49, 50))
    print(grafen.get_vekt(50, 51))