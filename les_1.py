from colorama import init, Fore
import math

print(Fore.GREEN + "Задача 0 (разминка)" + Fore.RESET)

a = [1, 0, 9, 12, 18, 34, 89, 91, 33, 127]
b = [2, 8, 9, 11, 76, 25, 44]

print("1. ", a[0], " ", a[2], " ", a[-1])

b.append(7)
print("2. ", b)

a[4] = 8
print("3. ", a)

c = a + b
print("4. ", c)

d = a[:-1] + [100]
print("5. ", d)
#############################################################

print(Fore.GREEN + "Задача 1 (девочковая)" + Fore.RESET)

girls = ["Иветта", "Виолетта", "Кассандра", "Вирджиния", "Амелия", "Розамунда", "Янина"]

girls1 = girls[1:5]
print("1. ", girls1)

girls2 = girls[3:7] + ["Беатриса"]
print("2. ", girls2)

girls3 = girls[:5]
girls3.remove("Кассандра")
print("3. ", girls3)

girls4 = [girls[2], girls[4], girls[5]]
print("4. ", girls4)
#############################################################

print(Fore.GREEN + "Задача 2 (поэлементная)" + Fore.RESET)
L = [12, 3, 8, 125, 10, 98, 54, 199]

print("1.")
for i in L:
    print("\t", i)
print()

for i in L:
    print("\t", math.log(i))

L[4] = 0
print("2.")
for i in L:
    if i > 0:
        print("\t", math.log(i))
    else:
        print("\tПринято считать, что логарифм можно вычислить только от положительного числа.")
#############################################################

