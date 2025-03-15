from colorama import Fore

print(Fore.GREEN + "Задание 1 (весеннее)" + Fore.RESET)
n = int(input(Fore.YELLOW + "Введите номер дня: " + Fore.RESET))

minutes = 1 + 3 * (n - 1)
print(f"День {n}: {minutes} минут")
#############################################################

print(Fore.GREEN + "Задание 2 (приветственное)" + Fore.RESET)

name = str(input(Fore.YELLOW + "Введите фамилию и имя: " + Fore.RESET))
print(f"{name}, добро пожаловать!")
#############################################################

print(Fore.GREEN + "Задание 3 (кулинарно-политологическое)" + Fore.RESET)
course1 = str(input(Fore.YELLOW + "Введите название курса 1: " + Fore.RESET))
course2 = str(input(Fore.YELLOW + "Введите название курса 2: " + Fore.RESET))
course3 = str(input(Fore.YELLOW + "Введите название курса 3: " + Fore.RESET))

template = (f"{course1} : 200 г\n"
            f"{course2} : 300 г\n"
            f"{course3} : 100 г\n")
print(template)
#############################################################

print(Fore.GREEN + "Задание 4 (кулинарно-математическое)" + Fore.RESET)
weight1 = int(input(Fore.YELLOW + "Введите вес первого ингредиента: " + Fore.RESET))
weight2 = int(input(Fore.YELLOW + "Введите вес второго ингредиента: " + Fore.RESET))
weight3 = int(input(Fore.YELLOW + "Введите вес третьего ингредиента: " + Fore.RESET))

recipe = ("Рецепт:\n"
            f"политическая теория : {weight1}\n"
            f"история политических учений: {weight2}\n"
            f"математика: {weight3}\n"
            "Приправить политической историей. Добавить математические модели по вкусу.")
print(recipe)