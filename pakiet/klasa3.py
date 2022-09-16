class Tesla:
    def __init__(self):
        self.__silnik = False
        self.__bieg = 0
        self.__predkosc = 0

    def uruchom(self):
        self.__silnik = True

    def wylacz(self):
        self.__silnik = False

    def __biegNastepny(self):
        if self.__bieg <= 6:
            self.__bieg += 1
            print("Bieg", self.__bieg)

    def __biegPoprzedni(self):
        if self.__bieg >= 0:
            self.__bieg -= 1
            print("Bieg", self.__bieg)

    def przyspiesz(self):
        if self.__silnik == True:
            self.__predkosc += 10
            print("Prędkość", self.__predkosc)
            self.__biegNastepny()

    def hamuj(self):
        if self.__predkosc >= 10:
            self.__predkosc -= 10
        else:
            self.__predkosc = 0
            print("Prędkość", self.__predkosc)
            self.__biegPoprzedni()

car = Tesla()
car.uruchom()
car.przyspiesz()
# car.__predkosc = 1500
car.przyspiesz()
# car.__bieg = 8979
car.hamuj()


