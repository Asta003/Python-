questions = [

    ("Сколько будет 2 + 2?", ["3", "4", "5"], "4"),

    ("Какой год начала Великой Отечественной войны?", ["1941", "1939", "1945"], "1941"),

    ("Чему равен sin(90°)?", ["0", "1", "√2/2"], "1"),

    ("Какая планета ближе всего к Солнцу?", ["Венера", "Марс", "Меркурий"], "Меркурий"),

    ("Сколько сторон у треугольника?", ["2", "3", "4"], "3"),

    ("Кто автор 'Евгения Онегина'?", ["Пушкин", "Лермонтов", "Гоголь"], "Пушкин"),

    ("Какой элемент обозначается символом O?", ["Железо", "Кислород", "Золото"], "Кислород"),

    ("Сколько дней в феврале в високосном году?", ["28", "29", "30"], "29"),

    ("Как называется столица Франции?", ["Лондон", "Берлин", "Париж"], "Париж"),

    ("Какое число делится на 2 и на 3 без остатка?", ["4", "6", "7"], "6")

]

for i, (q, opts, correct) in enumerate(questions, 1):

    print(f"Вопрос {i}: {q}")

    for j, opt in enumerate(opts, 1):

        print(f"{j}. {opt}")

    try:

        ans = int(input("Введите номер ответа: "))

        if 1 <= ans <= 3 and opts[ans - 1] == correct:

            print("Правильно")

        else:

            print("Не правильно")

    except:

        print("Не правильно")

    print()

# 2 ///

print("Решение квадратного уравнения ax^2 + bx + c = 0")

a = float(input("Введите коэффициент a: "))

b = float(input("Введите коэффициент b: "))

c = float(input("Введите коэффициент c: "))

D = b**2 - 4*a*c

print(f"\nУравнение: {a}x^2 + {b}x + {c} = 0")

print(f"Дискриминант D = {D}")

if D > 0:

    x1 = (-b + D**0.5) / (2*a)

    x2 = (-b - D**0.5) / (2*a)

    print(f"Уравнение имеет два корня:")

    print(f"x1 = {x1}")

    print(f"x2 = {x2}")

elif D == 0:

    x = -b / (2*a)

    print(f"Уравнение имеет один корень (два одинаковых):")

    print(f"x = {x}")

else:

    print("Уравнение не имеет действительных корней")

# 3///

total = 0

count = 0

while True:

    num = int(input())

    if num == 100:

        break

    if num % 2 == 0:

        total = total + num

        count = count + 1

if count > 0:

    average = total / count

    print(average)

else:

    print(0)

# 4///

text = input("Введите слова через пробел: ")

words = text.split()

all_good = True

for word in words:

    first_letter = word[0].upper()

    if first_letter not in ['A', 'B', 'C']:

        all_good = False

        break

if all_good and len(words) > 0:

    print("YES")

else:

    print("NO")