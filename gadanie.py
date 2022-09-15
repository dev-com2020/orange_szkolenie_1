import random

r = random.random() * 100
print(int(r))

k6 = random.randrange(1, 6)  # 1-5
k6_3 = random.randrange(100)  # 1-5
k6_2 = random.randint(1, 6)  # 1-6
print(k6)
print(k6_2)
print(k6_3)


l = ["tomek", "ania", "karolina"]

losowanie = random.choice(l)
print(losowanie)
