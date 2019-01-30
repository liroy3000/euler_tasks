"""
Задача проекта Эйлера
https://projecteuler.net/problem=6

Сумма квадратов первых десяти натуральных чисел равна

1^2 + 2^2 + ... + 10^2 = 385
Квадрат суммы первых десяти натуральных чисел равен

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет 3025 − 385 = 2640.

Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
"""

sumk = 0
ksum = 0

for i in range(1, 101):
	sumk = i * i + sumk

for i in range(1, 101):
	ksum = ksum + i
ksum = ksum * ksum

result = ksum - sumk
print(result)
