"""
Задача проекта Эйлера
https://projecteuler.net/problem=3

Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""

import math
integer = 600851475143

def isprime(i):
	"""
	Функция проверяет, является ли входное число простым
	"""
	limit = math.ceil(math.sqrt(i))
	result = True
	for j in range(2, limit):
		if i % j == 0:
			result = False
			break
	return result


for i in range(2, integer):
	if integer % i == 0:
		delimeter = integer / i
		print(delimeter)
		if isprime(delimeter):
			max_delimeter = delimeter
			break


print(max_delimeter)