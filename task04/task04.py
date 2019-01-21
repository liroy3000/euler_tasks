"""
Задача проекта Эйлера
https://projecteuler.net/problem=3

Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. 
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""

def ispolidrom(i):
	i = str(i)
	if len(i) % 2 !=0:
		return False

	if i[:int(len(i) / 2)] != i[len(i):int(len(i) / 2 - 1): -1]:
		return False
	else:
		return True

polindrom = []

for i in range(999, 99, -1):
	for j in range(999, 99, -1):
		if ispolidrom(i * j):
			polindrom.append(i * j)
			break

print(max(polindrom))