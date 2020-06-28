#!/root/python/hh1h/bin/python

"""
Дебильный калькулятор v1
"""

what = input("Что делаем? (+, -): ")

a = int(input("Введи первое число: "))
b = int(input("Введи второе число: "))

if what == "+":
	ab = str(a + b)
	print("Результат: " + ab)
elif what == "-":
	ab = str(a - b)
	print("результат: " + ab)
else:
	print("Неверная операция!")


print("Hello, world")

