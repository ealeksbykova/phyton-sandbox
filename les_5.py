from colorama import Fore
import math

print(Fore.GREEN + "Задача 1" + Fore.RESET)

def square(number, return_value=False):
    result = number ** 2

    print(f"Квадрат числа равен: {result}")

    if return_value:
        return result

square(5)

print(f"Возвращённый результат: {square(5, return_value=True)}")
#############################################################

print(Fore.GREEN + "Задача 2" + Fore.RESET)

def nums(number):
    return [number - 1, number + 1]

print(nums(7))
#############################################################

print(Fore.GREEN + "Задача 3" + Fore.RESET)

def str_lower(input_str):
    return [word.lower() for word in input_str.split()]

print(str_lower("В лесу родилась ёлочка В лесу она росла"))
#############################################################

print(Fore.GREEN + "Задача 4" + Fore.RESET)

def my_log(numbers):
    return [math.log(num) if num > 0 else None for num in numbers]

numbers = [1, 3, 2.5, -1, 9, 0, 2.71]
print(my_log(numbers))
#############################################################

print(Fore.GREEN + "Задача 5" + Fore.RESET)

def create_dict(names, ages):
    if len(names) == len(ages):
        return dict(zip(names, ages))
    else:
        print("Списки имеют разную длину")
        return {}

names1 = ["Ann", "Tim", "Sam"]
ages1 = [12, 23, 17]
print(create_dict(names1, ages1))

names2 = ["Ann", "Tim", "Sam"]
ages2 = [12, 23, 17, 45]
print(create_dict(names2, ages2))
#############################################################

print(Fore.GREEN + "Задача 6" + Fore.RESET)

def binomial_coeff(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def binom_prob(p, n, k):
    binom_coefficient = binomial_coeff(n, k)

    return binom_coefficient * (p ** k) * ((1 - p) ** (n - k))

p = 0.5
n = 10
k = 3

result = binom_prob(p, n, k)
print(f"Вероятность того, что будет ровно {k} успехов: {result}")
#############################################################

print(Fore.GREEN + "Задача 7" + Fore.RESET)

def all_sort(*args):
    return sorted(args)

print(all_sort(7, 6, 1, 3, 8, 0, -2))
