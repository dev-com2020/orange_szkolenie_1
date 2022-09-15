pi = 3.14

def rysunek():
    '''funkcja która rysuje ludzika'''
    print('''
                <______>
                < -  - >
                <   *  >
                --------
    ''')


def powitanie():
    imie = input("Podaj swoje imię: ")
    print("Cześć!", imie)


def powitanie2(imie="domyślny"):
    ''' Witaj się z użytkownikiem!'''
    print("Cześć!", imie)


def promien(r):
    global pi
    pi = 4.45
    return (pi * r * r)

