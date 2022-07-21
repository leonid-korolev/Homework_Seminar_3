# задача_1
# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов
# списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 
# 3 и 9, ответ: 12
 
def sum_of_elements():
    list = [2,3,5,9,3]
    print(list)
    positions = f'на нечётных позициях элементы {list[1: :2]}'
    s = f'ответ: {sum(list[1: :2])}'
    return positions,s 
   
print(sum_of_elements())


# Задача_2
# Напишите программу, которая найдёт произведение
# пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# Формирование списка целых чисел с проверкой на ввод чисел.
def get_number():
    while True:
        try:
            print('Введите несколько чисел через пробел')
            my_list = [int(i) for i in input() .split()]
            print(my_list)
            return my_list        
        except ValueError:
            print('Вы ввели не числа, повторите ввод')
            
# Произведение пар чисел списка.
def pairs_of_numbers(list: list):
    new_list = []
    for i in range(0, (len(list) + 1) // 2):
        new_list.append(list[i]*list[-i-1])
    print(new_list)
    
result = get_number()
pairs_of_numbers(result)


# Задача_3 
# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.567, 10.003] => 0.564 или 564

my_list = [1.1, 1.2, 3.1, 5.567, 10.003]
print(my_list)

def null_counter(num:float):
    counter = 0
    while num != int(num):
        num*=10
        counter+=1
    return counter, num

def change_list(my_list: list):
    max_counter = 0
    counters_list = []
    for i in range(len(my_list)):
        counter,num = null_counter(my_list[i])
        counters_list.append(counter)
        my_list[i] = num
        if counter > max_counter:
            max_counter = counter
    for i in range(len(counters_list)):
        counter = max_counter - counters_list[i]
        if counter:
            my_list[i] *= 10**counter
    return my_list, max_counter

def difference_max_min(my_list):
    my_list, max_counter = change_list(my_list)
    print(my_list, max_counter)
    max_num, min_num = 0,my_list[0]
    for num in my_list:
        float_part=num % 10**max_counter
        if float_part > max_num:
            max_num = float_part
        if float_part < min_num:
            min_num = float_part
    print(f'{max_num=},{min_num=}')
    return max_num - min_num, (max_num - min_num)/10**max_counter

print(difference_max_min(my_list))


# Задача_4
# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def get_number():
    while True:
        n = input('Введите целое положительное число: ')
        try:
            n = int(n)
            if n <= 0:
                print('Это отрицательное число')
            else:
                return n
        except ValueError:
            print('Некорректный ввод')
        
n = get_number()

def decimal_binary(n):
	result = ''
	while n > 0:
		result = str(n % 2) + result
		n //= 2
	return result

decimal_binary(n)
print(f'{n} ->', decimal_binary(n))


# Задача_5 
# Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так:
#  [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

def get_namber():
    while True:
        k = input('Введите число членов последовательности Фибоначчи: ')
        try:
            k = int(k)
            return k
        except ValueError:
            print('Некорректный ввод')
        
k = get_namber()
print(f'k =',k)

def fibonacci(k):
    n = abs(k)
    fibonacci = [0,1]
    for i in range(n -1):
        fibonacci.append(fibonacci[i] + fibonacci[i + 1])
    
    nega_fibonacci = [0,1]
    for i in range(n -1):
        nega_fibonacci.append(nega_fibonacci[i] + nega_fibonacci[i + 1]*-1)

    fibonacci_list = nega_fibonacci[len(nega_fibonacci):0:-1] + fibonacci

    print(fibonacci_list)

fibonacci(k)