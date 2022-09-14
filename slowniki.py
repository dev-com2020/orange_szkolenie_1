slownik1 = {1: "pierwszy",
            2: "drugi",
            "imie": "Tomek",
            "wiek": 39
            }
print(type(slownik1))
slownik1[1] = "jeden"
slownik1["imie"] = "Krzysiek"
slownik1["nazwisko"] = "Kowalski"
print(slownik1)
print(slownik1.keys())
print(slownik1.values())
print(slownik1[2])

lotek = {1, 3, 1, 4, 5, 9, 5}
print(type(lotek))
print(lotek)
print(5 in lotek)