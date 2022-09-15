# r - odczyt
# a - dopisanie
# w - zapisanie

lista = ["Tomek", "Marcin", "Krzysiek", "Żaneta"]

uchwyt = open('plik.log', 'a', encoding='utf-8')
# uchwyt2 = open(r'C:\Users\razor\notatki\tomek\plik.txt')
# uchwyt3 = open('C:\Users\\razor\\notatki\\tomek\plik.txt')
# dane = uchwyt.read()
#
# for i in lista:
#     uchwyt.write(i)
#     uchwyt.write("\n")
#     print(i)
dane = uchwyt.write("\nKarolina")
# print(dane)
uchwyt.close()

l = []

with open('plik.log', 'r', encoding='utf-8') as odczyt:
    for i in odczyt:
        l.append(i)

print(l[1])
