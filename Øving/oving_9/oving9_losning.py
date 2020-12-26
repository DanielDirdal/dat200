from grafer.graf_nabolister import GrafNaboliste
from grafer.dijkstra import dijkstra, skriv_utkorteste_vei

def les_kartfil(filnavn):
    with open(filnavn) as fila:
        bredde = int(fila.readline().strip())
        hoyde = int(fila.readline().strip())
        startx = int(fila.readline().strip())
        starty = int(fila.readline().strip())
        sluttx = int(fila.readline().strip())
        slutty = int(fila.readline().strip())
        rader = []
        for i in range(hoyde):
            rader.append([])
            linje = fila.readline()
            celler = linje.split(",")
            for celle in celler:
                verdi = int(celle.strip())
                rader[i].append(verdi)
        return bredde, hoyde, startx, starty, sluttx, slutty, rader


def nodeindeks_utregning(x, y, bredde):
    return y*bredde + x


def bygg_graf(hoyde, bredde, terrengmatrise):
    grafen = GrafNaboliste()
    for y in range(hoyde):
        for x in range(bredde):
            grafen.add_node(f"({x}, {y})")
    for y in range(hoyde-1):
        for x in range(bredde):
            node_indeks = nodeindeks_utregning(x, y, bredde)
            vertikal_nabo_indeks = nodeindeks_utregning(x, y+1, bredde)
            grafen.add_edge(node_indeks, vertikal_nabo_indeks, abs(terrengmatrise[y][x] - terrengmatrise[y+1][x]) + 1)
            grafen.add_edge(vertikal_nabo_indeks, node_indeks, abs(terrengmatrise[y][x] - terrengmatrise[y+1][x]) + 1)
            if x < bredde-1:
                horisontal_nabo_indeks = nodeindeks_utregning(x+1, y, bredde)
                grafen.add_edge(node_indeks, horisontal_nabo_indeks, abs(terrengmatrise[y][x] - terrengmatrise[y][x+1]) + 1)
                grafen.add_edge(horisontal_nabo_indeks, node_indeks, abs(terrengmatrise[y][x] - terrengmatrise[y][x + 1]) + 1)
    return grafen


if __name__ == "__main__":
    bredde, hoyde, startx, starty, sluttx, slutty, rader = les_kartfil("oving_9_eksempelfil.txt")
    print("Bredde: " + str(bredde))
    print("Høyde: " + str(hoyde))
    print(f"Startposisjon: ({startx}, {starty})")
    print(f"Sluttposisjon: ({sluttx}, {slutty})")
    for rad in rader:
        for kolonne in rad:
            print(f" {kolonne:2d}", end="")
        print()
    grafen = bygg_graf(hoyde, bredde, rader)
    fra_index = nodeindeks_utregning(startx, starty, bredde)
    til_index = nodeindeks_utregning(sluttx, slutty, bredde)
    lengde = dijkstra(grafen, fra_index, til_index)
    print(f"Lengden til veien: {grafen.get_kostnad(til_index)}")
    print(f"Til node: {grafen.get_nodedata(til_index)}")
    skriv_utkorteste_vei(grafen, til_index)

    print()
    print(grafen.get_vekt(49, 50))
    print(grafen.get_vekt(50, 51))