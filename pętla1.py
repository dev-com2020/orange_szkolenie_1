# while (dopóki) warunek:
#   ciało pętli
# else:
#   kod który, gdy warunek nie jest spełniony

licznik = 0
while licznik < 5:
    print(licznik, "mniejszy od 5")
    # licznik = licznik + 1
    licznik += 1
    if licznik == 3:
        break
# print("Poza pętlą!")
print(licznik)




if licznik == 5:
    print(licznik, "równe 5")
elif licznik > 6:
    print(licznik, "większe od 6")
    if licznik == 10:
        print("Licznik jest 10...")
elif licznik < 4:
    print(licznik, "w instrukcji if mniejsze od 4")
else:
    print("Ja tu sobie jestem else...")

