from abc import ABC, abstractmethod


class Ptak(ABC):
    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print("Tu", self.gatunek, "Startuje i osiągam prędkość max:", self.szybkosc)

    @abstractmethod
    def wydajOdglos(self):
        pass


class Orzel(Ptak):

    def poluj(self):
        print("Tu", self.gatunek, "Rozpocznam polowanie!")

    def wydajOdglos(self):
        print("Piiiii")


class Kogut(Ptak):

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def dziubaj(self):
        print("Tu", self.gatunek, "rozpoczynam dziubanie...")

    def lataj(self):
        print("Tu", self.gatunek, "Ja nie latam :(")

    def wydajOdglos(self):
        print("Kukuryku")





p1 = Orzel("bielik", 100)
p1.poluj()
p1.lataj()
p1.wydajOdglos()

p2 = Kogut("franek")
p2.dziubaj()
p2.lataj()
p2.wydajOdglos()
