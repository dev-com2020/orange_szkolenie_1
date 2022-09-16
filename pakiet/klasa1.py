class Human:

    def __init__(self, imie, wiek=0, plec="m"):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def przywitaj(self):
        print("Cześć, mam na imię", self.imie)

    def ruszaj(self):
        if self.plec == 'k':
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")

    def mysl(self):
        if self.wiek < 2:
            print("Dopiero się uczę")
        else:
            print("2+2=4")
