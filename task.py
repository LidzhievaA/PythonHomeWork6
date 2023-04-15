# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# elem_count = int(input("Введите  колличество элементов массива: "))
# first_elem = int(input("Введите первый элемент массива: "))
# progression_diff = int(input("Введите разность прогрессии: "))
# progression_arr = []

# def progression(elem_count, first_elem, progression_diff):
    
#     for n in range (1, elem_count + 1):
#         progression_arr.append(first_elem + (n-1) * progression_diff)
        
#     print(progression_arr)


# progression(elem_count, first_elem, progression_diff)


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и 
# не больше заданного максимума)

# input_list = [13, 45, 7, 89, 4, 0, 12, 9]
# min_num = int(input("Введите минимальное значение диапозона: "))
# max_num = int(input("Введите максимальное значение диапозона: "))
# for i in range(len(input_list)):
#     if min_num < input_list[i] < max_num:
#         print (i)