# int = liczby całkowite: 2,34,-54, 44545454545
# float = liczby zmiennoprzecinkowe: 5.5
# complex = liczba zespolona: 3 + 2j -4 -4.4j
# wartość logiczna = bool: True=1, False=0

# print(5 / 2)  # dzielenie z resztą
# print(5 // 2)  # dzielenie
# print(5.5 * 2)  # mnożenie
# print(5 ** 2)  # potęgowanie
# print(5 * -2 + (4 * 5) - 43)
# print(" * " * 10)  # tak też się da :)
# print('Hej, jestem "Python"')  # typ string
# print(["jeden", 7.7, "dwa", "trzy", [4, 5, 6], 8.8, 9.9])  # typ lista
#
# imie = int("5")  # zmienna
# # imie = "5"
# print(type(imie))  # sprawdzanie typu
#
# WIEK = 39  # to też jest zmienna
# print(WIEK)
#
# lista = ["jeden", 7.7, "dwa", "trzy", [4, 5, 6], 8.8, 9.9]
# print(type(lista))
# print(lista[4][1])  # wycinek (lista wielowymiarowa)
# print(lista[0:3])  # wycinek
# print(lista[0], lista[5])
# print(lista[-3:])  # wycinek od końca
# lista[0] = 1  # podmiana
# lista.append("Tomek")  # dodanie na końcu listy
# lista.append("Tomek")  # dodanie na końcu listy
# lista.insert(2, "Artur")  # dodanie w dany indeks
# lista.remove("dwa")  # usunięcie po zawartości
# lista.pop(1)  # usunięcie po indeksie
# # lista.clear() # czyszczenie do zera
# lista.index("trzy", 1, 5)  # sprawdzanie czy znajduję się w zakresie
# print(len(lista))  # długość listy
# # print(lista)
# print(lista.count("Tomek"))  # ile razy występuje?

liczby = [4, 66, 2, 6432, 76, 1]
imiona = ["Tomek", "Adam", "Adamina", "Joanna"]
print(liczby)
liczby.sort()
print(liczby)
liczby.reverse()
print(liczby)
print(imiona)
imiona.sort()
print(imiona)
imiona.reverse()
print(imiona)
print(min(imiona))
print(max(imiona))

napis = "Krzysztof Kowalski"
print(napis.count("K"))
print(napis[0:5])
print(napis.capitalize())
print(napis.upper())
print(napis, "wita...", 4, "razy")
print(napis + " wita..." + " 4 razy")

