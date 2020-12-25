class Edge:
    def __init__(self, til_node, vekt, type=None):
        self.til_node = til_node
        self.vekt = vekt
        self.type = type

class Node:
    def __init__(self, dataobjekt, type, kostnad=None):
        self.dataobjekt = dataobjekt
        self.kostnad = kostnad
        self.starttidspunt = 0
        self.sluttidspunkt = 0
        self.naboer = {}        # Dict: nodeindeks -> kantobjekt
        self.forrige_node = None
        self.type = type

class GrafNaboliste:
    def __init__(self):
        self.noder = []

    def add_node(self, dataobjekt, type):
        ny_node = Node(dataobjekt, type)
        self.noder.append(ny_node)
        return len(self.noder)-1

    def add_edge(self, fra_node, til_node, vekt):
        noden = self.noder[fra_node]
        noden.naboer[til_node] = Edge(til_node, vekt)

    def get_nodedata(self, node_referanse):
        return self.noder[node_referanse].dataobjekt

    def get_vekt(self, fra_node, til_node):
        noden = self.noder[fra_node]
        try:
            vekt = noden.naboer[til_node].vekt
        except KeyError:
            vekt = None
        return vekt

    def set_kostnad(self, node_referanse, kostnad):
        noden = self.noder[node_referanse]
        noden.kostnad = kostnad

    def get_kostnad(self, node_referanse):
        noden = self.noder[node_referanse]
        return noden.kostnad

    def fjern_kostnader(self):
        for node in self.noder:
            node.kostnad = None
            node.starttidspunkt = 0
            node.sluttidspunkt = 0
            node.forrige_node = None

    def fjern_kanttyper(self):
        for node in self.noder:
            for til_node in node.naboer:
                kant = node.naboer[til_node]
                kant.type = None

    def get_antall_noder(self):
        return len(self.noder)

    def get_naboer(self, node_referanse):
        naboliste = []
        for node_indeks in self.noder[node_referanse].naboer:
            naboliste.append(node_indeks)
        return naboliste

    def set_kant_type(self, fra_node, til_node, type):
        noden = self.noder[fra_node]
        kant = noden.naboer[til_node]
        kant.type = type

    def get_kant_type(self, fra_node, til_node):
        noden = self.noder[fra_node]
        kant = noden.naboer[til_node]
        return kant.type

    def get_starttidspunkt(self, node):
        noden = self.noder[node]
        return noden.starttidspunkt

    def get_sluttidspunkt(self, node):
        noden = self.noder[node]
        return noden.sluttidspunkt

    def set_starttidspunkt(self, node, tidspunkt):
        noden = self.noder[node]
        noden.starttidspunkt = tidspunkt

    def set_sluttidspunkt(self, node, tidspunkt):
        noden = self.noder[node]
        noden.sluttidspunkt = tidspunkt

    def get_forrige_node(self, node):
        noden = self.noder[node]
        return noden.forrige_node

    def set_forrige_node(self, node, forrige):
        noden = self.noder[node]
        noden.forrige_node = forrige

