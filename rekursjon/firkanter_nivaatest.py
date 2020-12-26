import tkinter


ANTALL_NIVAAER = 8


# Første eksempel på en fraktal: Tegner en firkant i midten og så en mindre firkant i hvert
# hjørne til den større firkanten. Gjør det mange nok ganger, og mønsteret som trer fram likner lite
# på firkanter.
class FirkantStjerne:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.tegner = tkinter.Canvas(self.hovedvindu, width=600, height=600)
        self.tegner.pack()
        self.rekursiv_tegner(150, 300, 300, ANTALL_NIVAAER)
        tkinter.mainloop()

    def rekursiv_tegner(self, storrelse, senter_x, senter_y, antall_nivaaer):
        if antall_nivaaer <= 0:
            return
        self.tegner.create_rectangle(senter_x-storrelse, senter_y-storrelse, senter_x+storrelse, senter_y+storrelse, fill="black")
        self.rekursiv_tegner(storrelse//2, senter_x-storrelse, senter_y-storrelse, antall_nivaaer-1)
        self.rekursiv_tegner(storrelse//2, senter_x+storrelse, senter_y-storrelse, antall_nivaaer-1)
        self.rekursiv_tegner(storrelse//2, senter_x-storrelse, senter_y+storrelse, antall_nivaaer-1)
        self.rekursiv_tegner(storrelse//2, senter_x+storrelse, senter_y+storrelse, antall_nivaaer-1)


if __name__ == "__main__":
    gui = FirkantStjerne()
