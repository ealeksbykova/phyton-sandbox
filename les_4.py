from colorama import Fore

print(Fore.GREEN + "Задача 1" + Fore.RESET)

rept = {"python": "питон", "anaconda": "анаконда", "tortoize": "черепаха"}

rept["snake"] = "змея"
rept["tortoise"] = rept.pop("tortoize")

for key, value in rept.items():
    print(f"{value.capitalize()} по-английски будет {key}.")
#############################################################

print(Fore.GREEN + "Задача 2" + Fore.RESET)

cnt = ["Andorra", "Belarus", "Denmark", "Kenya", "Jamaica", "Romania"]
fh = [1.0, 6.0, 1.0, 4.0, 2.5, 2.0]

print(dict(zip(cnt, fh)))

#############################################################

print(Fore.GREEN + "Задача 3" + Fore.RESET)

pairs = [(2, 4), (4, 6), (0, 1), (5, 2), (9, 1), (3, 8)]

print({pair: pair[0] * pair[1] for pair in pairs})
#############################################################

print(Fore.GREEN + "Задача 4" + Fore.RESET)

grades = {'Anna': 4, 'Bob': 3, 'Claire': 5, 'Dick': 2, 'Elena': 5,
          'Fred': 5, 'George': 4, 'Kristina': 3, 'Nick': 2,
          'Ursula': 4, 'Viktor': 5}

excel = []
good = []
satisf = []
bad = []

for student, grade in grades.items():
    print(f"{student}: {grade}")
    if grade == 5:
        excel.append(student)
    elif grade == 4:
        good.append(student)
    elif grade == 3:
        satisf.append(student)
    else:
        bad.append(student)

print()
print("Студенты с отличными оценками:", excel)
print("Студенты с хорошими оценками:", good)
print("Студенты с удовлетворительными оценками:", satisf)
print("Студенты с плохими оценками:", bad)
