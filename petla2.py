# lista = []
# print("Podaj liczby, które chcesz wrzucić do listy")
# print("Wpisz STOP aby zakończyc program!")
#
# while True:
#     wejscie = input("Wprowadź liczbę:")
#     if wejscie == 'stop':
#         break
#     lista.append(int(wejscie))
#
# print("Twoja lista -> ", lista)

# lista2 = [4, 5, 6]
#
# for i in lista2:
#     print("Element listy: ", i)
#
# for i, j in enumerate(lista2):
#     print("Indeks:", i, "Element listy: ", j)
#
# slownik = {"imie": "Marek", "nazwisko": "Kowalski", "plec": "mezczyzna"}
#
# for i in slownik:
#     print(i)
#
# for i in slownik.values():
#     print(i)
#
# for key, val in slownik.items():
#     print(key, "-->", val)
#
# for i in range(0, 6, 2):
#     print(i)

# x = [1, 3, -7, 9, -4, 4]
# for i in range(len(x)):
#     if x[i] < 0:
#         print("Znaleziono liczbę ujemną", i)


x = [1, 3, -7, 9, -4, 4]
for i in range(len(x)):
    if x[i] < 0:
        print("Znaleziono liczbę ujemną na indeksie", i)

# comprehension (generatory)
y = [i for i in range(3, 7)]
print(y)

z = ["2", "45", "55", "5"]
liczby = [int(i) for i in z]
print(liczby)

slownik = {1: "Burek", 2: "Azor", 3: "Fafik"}
print({value: key for key, value in slownik.items()})

zbior = [1, 2, 3, 3, 3, 3, 4, 4, 4, 5]
zbior2 = {i * 2 for i in zbior}
print(zbior2)

for i in range(-10, -1, 2):
    print(i)

for i in range(-1, -10, -2):
    print(i)