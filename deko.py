def wykonaj(funkcja, a, b):
    x = funkcja(a, b)
    return x


def dodaj(a, b):
    return a + b


def odejmij(a, b):
    return a - b


print(wykonaj(dodaj, 2, 3))


def glowna():
    def wewn(a, b):
        return a * b

    x = wewn(2, 3)
    return x


print(glowna())


def dekor(funkcja):
    def wew(*args, **kwargs):
        print("Dekorujemy funkcje")
        print(args, kwargs)
        return funkcja(*args, **kwargs)

    return wew


@dekor
def zwyklaFunkcja(a, b, c, **kwargs):
    print("To jest zwykła funkcja")

    print("Wynik:", a + b + c)


zwyklaFunkcja(1, 2, 3, wiek=39)
