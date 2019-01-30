"""
Задача проекта Эйлера
https://projecteuler.net/problem=5

2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?
"""

range_delim = [3,4,6,7,8,9,11,12,13,14,15,16,17,18,19]
def delimeter(j):
	result = True
	for i in range_delim:
		if j % i != 0:
			result = False
			break
	return result
i = 0
while True:
	print(i)
	if i == 0:
		i = i + 1
		continue
	if delimeter(i):
		print (i)
		break
	else:
		i = i + 10
