from grafer.demograf import bygg_demograf
from collections import deque

def bellman_ford(graf, startnode):
    nodekoe = deque()
    graf.fjern_kostnader()
    graf.set_kostnad(startnode, 0)
    nodekoe.append(startnode)
    while len(nodekoe) > 0:
        nv_node = nodekoe.popleft()
        graf.set_starttidspunkt(nv_node, graf.get_starttidspunkt(nv_node) + 1)
        if graf.get_starttidspunkt(nv_node)//2 > graf.get_antall_noder():
            raise ValueError("Negativ Sykel")
        naboer = graf.get_naboer(nv_node)
        for nabo in naboer:
            kostnad_til_nabo = graf.get_kostnad(nv_node) + graf.get_vekt(nv_node, nabo)
            if graf.get_kostnad(nabo) is None:
                graf.set_kostnad(nabo, kostnad_til_nabo)
                graf.set_forrige_node(nabo, nv_node)
                graf.set_starttidspunkt(nabo, graf.get_starttidspunkt(nabo) + 1)
                nodekoe.append(nabo)
            elif graf.get_kostnad(nabo) > kostnad_til_nabo:
                graf.set_kostnad(nabo, kostnad_til_nabo)
                graf.set_forrige_node(nabo, nv_node)
                if graf.get_starttidspunkt(nabo) % 2 == 0:
                    graf.set_starttidspunkt(nabo, graf.get_starttidspunkt(nabo) + 1)
                    nodekoe.append(nabo)

def skriv_utkorteste_vei(grafen, startnode):
    nv_node = startnode
    while nv_node is not None:
        print(f"Node: {grafen.get_nodedata(nv_node)}")
        nv_node = grafen.get_forrige_node(nv_node)

if __name__ == "__main__":
    grafen = bygg_demograf()
    bellman_ford(grafen, 0)
    print(f"Korteste vei fra A til H {grafen.get_kostnad(7)}")
    skriv_utkorteste_vei(grafen, 7)