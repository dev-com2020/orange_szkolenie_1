while True:

    wybor = int(input('''
        Witaj w kalkulatorze!
        Wybierz opcje:
        1. dodaj
        2. odejmij
        3. podziel
        4. opuść program
        
Wprowadź swój wybór:
    '''))


    # wybor = int(input("Podaj opcję (1-3): "))

    def dodaj(a, b):
        print("dodaje...")
        c = a + b
        print("Wynik =", c)


    def odejmij(a, b):
        print("odejmuje...")
        c = a - b
        print("Wynik =", c)


    def podziel(a, b):
        print("dzielenie...")
        c = a / b
        print("Wynik =", c)


    if wybor == 1:
        a = int(input("Podaj liczbę a"))
        b = int(input("Podaj liczbę b"))
        dodaj(a, b)
    elif wybor == 2:
        a = int(input("Podaj liczbę a"))
        b = int(input("Podaj liczbę b"))
        odejmij(a, b)
    elif wybor == 3:
        try:
            a = int(input("Podaj liczbę a"))
            b = int(input("Podaj liczbę b"))
            podziel(a, b)
        except ZeroDivisionError:
            print("Nastąpiło dzielenie przez 0")
    else:
        break
