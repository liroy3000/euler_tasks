"""
Задача проекта Эйлера
https://projecteuler.net/problem=6

Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
Какое число является 10001-ым простым числом?
"""
import math
def isprime(i):
	"""
	Функция проверяет, является ли входное число простым
	"""
	result = True
	for j in range(2, i):
		if i % j == 0:
			result = False
			break
	return result

i = 2
j = 0
while True:
	if isprime(i):
		j = j + 1
		if j == 10001:
			print(i)
			break
	i = i + 1
