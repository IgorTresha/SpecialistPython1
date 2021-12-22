# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр", ]
max_len = len(names[0])
for name in names:
    if len(name) > max_len:
        max_len = len(name)
for name in names:
    if max_len == len(name):
        print(name, ", ", end="")
