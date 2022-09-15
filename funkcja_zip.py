x = [1, 2, 3, 4]
y = ['a', 'b', 'c']
z = zip(x, y)
print(type(z))
# z = x + y
print(list(z))

x = 0
# if 0 < x < 10:
if 0 < x and x < 10:
    print("....")

if x < 10 or x > 15:
    print("...")

liczba = int(input("Podaj liczbę:"))
lista = [1, 3, 5, 7, 9]
if liczba not in lista:
    print("Nie ma na liście...")
else:
    print("Jest na liście")

