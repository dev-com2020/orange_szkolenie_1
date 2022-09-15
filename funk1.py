def duzo_rzeczy(data, *args, **kwargs):
    print(data)
    print(args)
    print(kwargs)


duzo_rzeczy(4, 55, 7.55, "Tomek", wiek=39)


def maksimum(*liczba):
    if len(liczba) == 0:
        return None
    else:
        liczba_max = liczba[0]
        for n in liczba[1:]:
            if n > liczba_max:
                liczba_max = n
        return liczba_max


w = maksimum()
print(w)
w1 = maksimum(3, 2, 8, -2, 45, 9)
print(w1)


def fun1(x, y, **inne):
    print("x: {0}, y: {1}, klucze w zmiennej inne: {2}".format(x, y, list(inne.keys())))
    inne_razem = 0
    for k in inne.keys():
        inne_razem = inne_razem + inne[k]
    print("Łącznie w zmiennej inne jest wartość {0}".format(inne_razem))


fun1(2, "1", liczb=34)
