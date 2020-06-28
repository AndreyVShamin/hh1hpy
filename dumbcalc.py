#!/root/python/hh1h/bin/python

from colorama import Fore, Back, Style

"""
Дебильный калькулятор v2
"""

print(Fore.GREEN)

what = input("Что делаем? (+, -): ")

print(Fore.CYAN)


a = float(input("Введи первое число: "))
b = float(input("Введи второе число: "))

print(Fore.YELLOW)


if what == "+":
	ab = str(a + b)
	print("Результат: " + ab)
elif what == "-":
	ab = str(a - b)
	print("результат: " + ab)
else:
	print("Неверная операция!")


print(Fore.YELLOW, Back.BLACK)

print("Hello, world")

