from grafer.graf_matrise import GrafMatrise
from grafer.graf_nabolister import GrafNaboliste

def bygg_demograf():
    grafen = GrafNaboliste()
    grafen.add_node("A")                # Indeks 0
    grafen.add_node("B")                # Indeks 1
    grafen.add_node("C")                # Indeks 2
    grafen.add_node("D")                # Indeks 3
    grafen.add_node("E")                # Indeks 4
    grafen.add_node("F")                # Indeks 5
    grafen.add_node("G")                # Indeks 6
    grafen.add_node("H")                # Indeks 7

    grafen.add_edge(0, 1, 5)
    grafen.add_edge(1, 0, 5)
    grafen.add_edge(0, 2, 2)
    grafen.add_edge(0, 3, 2)
    grafen.add_edge(3, 0, 2)

    grafen.add_edge(1, 2, 4)
    grafen.add_edge(2, 1, 4)
    grafen.add_edge(1, 4, 5)
    grafen.add_edge(4, 1, 5)

    grafen.add_edge(2, 6, 1)
    grafen.add_edge(6, 2, 3)

    grafen.add_edge(3, 6, 4)
    grafen.add_edge(6, 3, 4)
    grafen.add_edge(3, 7, 5)
    grafen.add_edge(7, 3, 5)

    grafen.add_edge(4, 5, 3)
    grafen.add_edge(5, 4, 3)
    grafen.add_edge(4, 6, 3)
    grafen.add_edge(6, 4, 3)

    grafen.add_edge(5, 6, 5)
    grafen.add_edge(6, 5, 5)

    grafen.add_edge(6, 7, 2)
    grafen.add_edge(7, 6, 2)
    return grafen

if __name__ == "__main__":
    grafen = bygg_demograf()
    print(grafen.get_nodedata(2))
    print(grafen.get_nodedata(0))
    print(grafen.get_nodedata(3))
    print(grafen.get_vekt(4, 5))
    print(grafen.get_vekt(5, 4))
    print(grafen.get_vekt(2, 6))
    print(grafen.get_vekt(6, 2))
    print(grafen.get_vekt(0, 7))
