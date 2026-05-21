n = 0

while n < 3:
    n = n + 1
    print("Hello")


n = 5
while n > 0:
    n += 1
    print(n)

import random
while True:
    n = random.randint(1, 10)
    print(n)
    if n == 7:
        break


n = 0

while n < 7:
    n = n + 1
    print("Пустой вокзал")

    
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))


while 0 < A < B:
    A = A + 1
    print(A, B)


while True:
    print("Купи слона!")
    phrase = input()
    print(f"Все говорят: {phrase}. А ты купи слона!")



import random

while True:
    n = random.randint(1, 7)
    num = int(input("Угадай число от 1 до 7: "))
    if num > n:
        print("меньше")
    elif num < n:
        print("больше")
    else:
        print("Поздравляю, ты угадал!")
        break


import random

while True:
    n = random.randint(1, 15)
    popitka = 3
    print("Угадай число от 1 до 15: ")
    while popitka > 0:
        num = int(input(f"Осталось попыток: {popitka}: "))
        if num > n:
            print("меньше")
        elif num < n:
            print("больше")
        else:
            print("Поздравляю, ты угадал!")
        
        popitka -= 1
    if popitka == 0:
        print("GAME OVER")