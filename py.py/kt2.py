# // 1

arr = list(range(1, 11))
print("Исходный массив:", arr)

arr_reversed = arr[::-1]
print("Перевёрнутый массив:", arr_reversed)



# // 2

import random
rows = int(input("Количество строк: "))
cols = int(input("Количество столбцов: "))

matrix = [[random.randint(-20, 20) for _ in range(cols)] for _ in range(rows)]
print("Матрица:")
for row in matrix:
    print(row)

min_elem = min(min(row) for row in matrix)
print("Минимальный элемент:", min_elem)

second_row = matrix[1] if rows >= 2 else []
print("Вторая строка:", second_row)

first_col = [row[0] for row in matrix] if cols >= 1 else []
print("Первый столбец:", first_col)

# /// 3

n = int(input("Длина массива: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Элемент {i+1}: ")))
print("Массив:", arr)

found = False
for i in range(len(arr) - 1):
    if arr[i] == 0 and arr[i + 1] == 0:
        found = True
        break

print("Есть два подряд идущих нуля:", "да" if found else "нет")


# // 4

import random
n = int(input("Длина массива: "))
arr = [random.randint(-50, 50) for _ in range(n)]
print("Массив:", arr)

evens = [x for x in arr if x % 2 == 0]
if evens:
    avg_even = sum(evens) / len(evens)
    count = sum(1 for x in arr if x % 3 == 0 and x == avg_even)
else:
    count = 0
    avg_even = None

print("Чётные числа:", evens)
print("Среднее арифметическое чётных:", avg_even)
print("Количество чисел, делящихся на 3 и равных этому среднему:", count)