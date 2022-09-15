import importlib
import sys

from pakiet import *
from tkinter import *
from pakiet import matma as m

# from pakiet.matma import rysunek

m.rysunek()
# m.powitanie()
m.powitanie2("tomek")
wynik = m.promien(2)
print(wynik)
print(m.pi)
print(m.powitanie2.__doc__)
print(importlib.reload(m))

wynik2 = test.dodaj(5, 5)
print(wynik2)
wynik3 = odejmij(6, 3)
print(wynik3)

print(sys.path)