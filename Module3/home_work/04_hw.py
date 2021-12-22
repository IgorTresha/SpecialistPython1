# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

import random

list_exampl = []
n = int(input("Введите n= "))
cnt = 0
while cnt < n:
    list_exampl.append(random.randint(-100, 100))
    cnt += 1
print("Дано: ", list_exampl)
new_list = []
for var in list_exampl:
    if var > 0 and var ** 0.5 % 1 == 0:
        new_list.append(round(var ** 0.5))
print("Answer: ", new_list)
