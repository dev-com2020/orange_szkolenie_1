# lambda <parametry> : <wyrażenie>

def dodaj(a, b):
    wynik = a + b
    return wynik


dodawanie = lambda a, b: a + b
print(dodawanie(2, 3))

temp = {"FnaK": lambda st_f: 273.15 + (st_f - 32) * 5 / 9, "CnaK": lambda st_c: 273.15 + st_c}

print(temp["FnaK"](32))
print(temp["CnaK"](32))

lista = [1, 3, 5, 7]
print(f"Zastosowanie map z lambda: {list(map(lambda _: _ * 2, lista))}")
print(f"Zastosowanie filter z lambda: {list(filter(lambda _: _ > 3, lista))}")


# F wyższego rzędu
def funkcja(f, liczba):
    print("Halloooo")
    return f(liczba)


def dodaj_jeden(x):
    return x + 1


def kwadrat(parametr):
    return parametr * parametr


# print(funkcja(dodaj_jeden, 7))
print(funkcja(lambda x: x + 1, 7))
# print(funkcja(kwadrat, 7))
print(funkcja(lambda x: x * x, 7))


def cztery():
    x = 0
    while x < 4:
        print("W generatorze x =", x)
        yield x
        x += 1

#
# for i in cztery():
#     print(i)


#
# print(2 in cztery())
# print(5 in cztery())

cztery()

def wznowienie():
    print("wstrzymuje")
    yield 1
    print("wzawiam")
    print("wstrzymuje")
    yield 2
    print("wzawiam")

gen = wznowienie()
print(type(gen))
#
# for i in wznowienie():
#     print("Zwrócono wartość:", i)

print(gen.__next__())
print(gen.__next__())
