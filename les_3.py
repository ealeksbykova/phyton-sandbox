from colorama import Fore

print(Fore.GREEN + "Задача 1" + Fore.RESET)

number = float(input(Fore.YELLOW + "Введите положительное число -> " + Fore.RESET))

if number > 0:
    print("Молодец!")
else:
    print("Это не положительное число.")
#############################################################

print(Fore.GREEN + "Задача 2" + Fore.RESET)

def get_marks(marks):
    for mark in marks:
        print(mark)

        if mark >= 9:
            print("Отлично")
        elif mark >= 7:
            print("Хорошо")
        elif mark >= 5:
            print("Удовлетворительно")
        else:
            print("Плохо")

marks = [10, 8, 6, 4, 9]
get_marks(marks)
#############################################################

print(Fore.GREEN + "Задача 3" + Fore.RESET)

correctPassword = "0000"
while True:
    if input(Fore.YELLOW + "Введите пароль -> " + Fore.RESET) == correctPassword:
        print("Login success")
        break
    else:
        print("Incorrect password, try again!")
#############################################################

print(Fore.GREEN + "Задача 4" + Fore.RESET)

favorNums = [3, 7, 11, 23, 18, 48, 81]

if int(input(Fore.YELLOW + "Введите целое число -> " + Fore.RESET)) in favorNums:
    print("Мое любимое число!")
else:
    print("Эх, ну почему?")
#############################################################

print(Fore.GREEN + "Задача 5" + Fore.RESET)

if int(input(Fore.YELLOW + "Введите число -> " + Fore.RESET)) % 2 == 0:
    print("Это число чётное")
else:
    print("Это число нечётное")
#############################################################

print(Fore.GREEN + "Задача 6" + Fore.RESET)

if input(Fore.YELLOW + "Введите существительное -> " + Fore.RESET)[0].isupper():
    print("Это имя собственное.")
else:
    print("Это имя нарицательное.")
