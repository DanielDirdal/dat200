from prioritetskoer.binaerhaug import Prioritetsko
from collections import deque
import random

HENDELSE_ANKOMMET = 1
HENDELSE_BEHANDLET = 2

MAKS_TID = 10000

PERSONBIL = 1
BOBIL = 2
BUSS = 3
LASTEBIL = 4

a_list = [PERSONBIL, BOBIL, BUSS, LASTEBIL]
distribution = [.75, .1, .05, .1]

def type_bil():
    antall = 0
    type = 0
    random_number = random.choices(a_list, distribution)
    if random_number == [1]:
        type = PERSONBIL
        antall = 1
    if random_number == [2]:
        type = BOBIL
        antall = 2
    if random_number == [3]:
        type = BUSS
        antall = 4
    if random_number == [4]:
        type = LASTEBIL
        antall = random.randint(3, 8)
    return type, antall

class Bil:
    def __init__(self, type, biltype, plass, tid):
        self.type = type
        self.biltype = biltype
        self.plass = plass
        self.tid = tid

    def __str__(self):
        return f"Biltype: {self.biltype} og bruker plass {self.plass}"


def bil_ankommer(passasjerer, hendelseskoe, systemtid):
    random_tid = random.randint(0, 60)
    ny_tid = systemtid + random_tid
    type, antall = type_bil()
    passasjerer.append(Bil(HENDELSE_ANKOMMET, type, antall, ny_tid))
    hendelseskoe.add(Bil(HENDELSE_ANKOMMET, type, antall, ny_tid), ny_tid)
    return random_tid, antall

def behandler_biler(passasjerer,hendelseskoe, ferge, tid):
    storrelse = ferge
    while True:
        if len(passasjerer) != 0 and passasjerer[0].plass <= storrelse:
            storrelse = storrelse - passasjerer[0].plass
            passasjerer.popleft()
        else:
            break
    ny_tid = tid + 1800
    hendelseskoe.add(Bil(HENDELSE_BEHANDLET, 1, 1, ny_tid), ny_tid)
    return storrelse, ny_tid


def kjor_simulering():
    hendelseskoe = Prioritetsko()
    passasjerer = deque()
    systemtid = 0
    koelengde = 0
    tid = 1800
    totalt_biler = 0

    maks_koelengde = 0
    fergestorresle = 80

    type, antall = type_bil()
    hendelseskoe.add(Bil(HENDELSE_ANKOMMET, type, antall, 0), 0)
    hendelseskoe.add(Bil(HENDELSE_BEHANDLET, type, antall, 1800), 1800)


    while systemtid < MAKS_TID:
        hendelse = hendelseskoe.remove()
        systemtid = hendelse.tid
        if hendelse.type == HENDELSE_ANKOMMET:
            tmp_tid, antall = bil_ankommer(passasjerer, hendelseskoe, systemtid)
            koelengde += antall
            print(f"Passasjer ankommer på tid: {systemtid} og koelengde er {koelengde}.")
            totalt_biler += 1
            if koelengde > maks_koelengde:
                maks_koelengde = koelengde
        if hendelse.type == HENDELSE_BEHANDLET:
            print(f"Båt ankommer og har kølengde på {koelengde}")
            tmp, ny_tid = behandler_biler(passasjerer, hendelseskoe, fergestorresle, tid)
            tid = ny_tid
            tmp_ko = fergestorresle - tmp
            koelengde = koelengde - tmp_ko
            print(f"Båt ankommer og har ny kølengde på {koelengde}, plasser som forsvant er {tmp_ko}")

    print("Simulering ferdig:")
    print(f"Maksimal kølengde: {maks_koelengde} og totalt biler er {totalt_biler}")

if __name__ == "__main__":
    kjor_simulering()