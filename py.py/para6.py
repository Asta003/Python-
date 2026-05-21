# num_1 = int(input("Введите число 1:"))
# num_2 = int(input("Введите число 2:"))
# num_3 = int(input("Введите число 3:"))
# num_4 = int(input("Введите число 4:"))
# if num_1 > num_2 & num_3 == num_4:
#     print(f"{num_1} > {num_2}")
# elif num_1 < num_2:
#     print(f"{num_1} < {num_2}")
# else:
#     print(f"{num_1} = {num_2}")

num = int(input("Введите целое число:"))
if num % 2 == 0:
    print(f"{num} - четное число")
else:
    print(f"{num} - нечетное число")

rost = int(input("Введите рост в см:"))
if rost > 120:
    print("Добро пожаловать!")
else:
    print("Извините, вы слишком малы.")

num1 = int(input("Введите любое число"))
if num1 > 0:
    print(f"{num1} - положительное число")
elif num1 < 0:
    print(f"{num1} - отрицательное число")
else:
    print(f"{num1} - ноль")

password = input("Введите пароль:")
if password == "secret123:":
    print("Пароль верный!")
else:
    print("Пароль неверный.")

sale = int(input("Введите сумму покупки:"))
if sale > 1000:
    discount = sale * 0.1
    print(f"Вы получили скидку 10%! Сумма со скидкой: {sale - discount}")
else:
    print("Скидка не предусмотрена.")

god = int(input("Введите год:"))
if god % 4 == 0 and (god % 100 != 0 or god % 400 == 0):
    print(f"{god} - високосный год")
else:
    print(f"{god} - не високосный год")

a = int(input("Введите число:"))
b = int(input("Введите число:"))
c = int(input("Введите число:"))
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Треугольник равносторонний")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")

x = float(input("Введите x:"))
y = float(input("Введите y:"))
if x == 0 and y == 0:
    print("Начало координат")
elif x == 0:
    print("Ось Y")
elif y == 0:
    print("Ось X")
elif x > 0 and y > 0:
    print("1-я четверть")
elif x < 0 and y > 0:
    print("2-я четверть")
elif x < 0 and y < 0:
    print("3-я четверть")
elif x > 0 and y < 0:
    print("4-я четверть")
else:
    print("Точка не принадлежит ни одной четверти")