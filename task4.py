# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = abs(int(input('Введите число n: ')))
prod = 1
list_n = []
for i in range(-n, n + 1): # заполнение списка
    list_n.append(i) # append добавление элемента в конец списка
print(list_n)    
with open('file.txt', 'r') as data: # открываем файл file.txt для чтения
    for line in data:
        prod *= list_n[int(line)] # перемножаем числа на позициях указанных в файле file.txt
print(prod)