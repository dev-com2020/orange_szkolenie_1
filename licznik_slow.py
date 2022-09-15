plik_wejsciowy = open('plik.log')
linie = plik_wejsciowy.read().split("\n")

liczba_linii = len(linie)
liczba_slow = 0
liczba_znakow = 0

for linia in linie:
    slowa = linia.split()
    liczba_slow += len(slowa)
    liczba_znakow += len(linia)

print("Plik ma {0} linie, {1} słow i {2} znaków".format(liczba_linii, liczba_slow, liczba_znakow))
