# Исходники размещены в репозитории по адресу: https://github.com/ealeksbykova/phyton-sandbox
from colorama import Fore
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

print(Fore.GREEN + "Задача 3 (демографическая)" + Fore.RESET)

age = [24, 35, 42, 27, 45, 48, 33]
ageSquares = []

for i in age:
    ageSquares.append(math.pow(i,2))

print("age: ", age)
print("ageSquares: ", ageSquares)
#############################################################

print(Fore.GREEN + "Задача 4 (игровая)" + Fore.RESET)
numbers = [1, 5, 6, 8, 10, 21, 25, 1, 0, -9, 9]
index = int(input(Fore.YELLOW + "Введите цифру от 1 до 10: " + Fore.RESET))
if 1<= index <= 10:
    print(numbers[index])
else:
    print(Fore.RED + f"Ввод некорректен: {index}" + Fore.RESET)
#############################################################

print(Fore.GREEN + "Задача 5 (мыслительная)" + Fore.RESET)
l = [1,2,3,4] # создание массив int
for i in range(len(l)): # генерация индексов от 0 до 3 по длине массива
    a = l[i] + l[i-1] # сложение текущего и предыдущего элементов массива по индексу. Индекс -1 указывает на последний элемент массива
    print(a) # вывод в stdout
