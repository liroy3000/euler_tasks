"""
Задача проекта Эйлера
https://projecteuler.net/problem=2

Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""
summ = 0
sequence = [1, 2]
while max(sequence) < 4000000:
	i = len(sequence)
	if sequence[i-1] % 2 == 0:
		summ = summ + sequence[i-1]
	sequence.append(sequence[i - 1] + sequence[i-2])

print(summ)