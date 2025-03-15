from colorama import Fore
import math

print(Fore.GREEN + "Задача 1" + Fore.RESET)
fullName = str(input(Fore.YELLOW + "Введите Ваши ФИО: " + Fore.RESET))
fullName = fullName.split(' ')

print(f"Ваша фамилия: {fullName[0]}")
print(f"Ваше имя: {fullName[0]}")
print(f"Ваше отчество: {fullName[0]}")
#############################################################

print(Fore.GREEN + "Задача 2" + Fore.RESET)

numString = str(input(Fore.YELLOW + "Введите числа через ; -> " + Fore.RESET))

numString = numString.replace(' ', '').split(';')

for num in numString:
    print(int(num))

for num in numString:
    print(float(num))
#############################################################

print(Fore.GREEN + "Задача 3" + Fore.RESET)

number = str(input(Fore.YELLOW + "Введите номер телефона через дефис -> " + Fore.RESET))

print(number.replace('-', ''))
#############################################################

print(Fore.GREEN + "Задача 4" + Fore.RESET)

def income_log(L):
    return [math.log(income) for income in L if income > 0]

L = [14000, 23000, -15000, 58000, 14500]
print(income_log(L))
#############################################################

print(Fore.GREEN + "Задача 5" + Fore.RESET)

def to_lower_case_out_of_whitespaces(words):
    return [word.lower().strip() for word in words]

words = ["Speak ", "to", "me ", "of", "Florence", "And ", "of", "the", "Renaissanc e"]
print(to_lower_case_out_of_whitespaces(words))
