# Задача 3. Задайте словарь из n чисел последовательности (1 + (1/n))^n
# и выведите на экран их сумму.
# Например:
# Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}

# Необходимо сложить все значения словаря и вывести  сумму на экран.

n = int(input('Введите число n: '))
dict_n = {}  # создаем пустой словарь
sum_dict = 0 # сумма значений словаря
for i in range(1, n + 1):
    dict_n[i] = round((1 + 1 / i)**i, 2)  # заполняем словарь по формуле (1 + (1/n))^n, round-ом округление до 2го знака посде запятой
    sum_dict += dict_n[i] # складываем значения словаря
print(f'Сумма всех значений словаря {dict_n} равна {round(sum_dict, 2)}')