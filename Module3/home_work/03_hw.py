# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here

import random

numbers = []
n = int(input("Введите n= "))
cnt = 0
while cnt < n:
    numbers.append(random.randint(-100, 100))
    cnt += 1
print(numbers)

total_summ = 0
for number in numbers:
    if number > 0 and number % 2 == 0:
        total_summ = total_summ + number
print("Сумма положительных элементов кратных 2 =", total_summ)
