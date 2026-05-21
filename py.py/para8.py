for i in range(4):
    print(i)

for i in range(3, 7):
    print(i)

for i in range(2, 9, 2):
    print(i)

for i in range(3, -1, -1):
    print(i)

for i in "hello world":
    print(i * 2, end='')


for i in range(1, 10, 3):
    if i == 7:
        print(">= 7 не использовать")
        break
    print(i)
else:
    print("Цикл завершился без прерывания")

for i in "hello world":
    if i == "o":
        continue
    print(i, end='')


start = 0
for i in range(1, 101):
    start += i
print(start)


for i in [3, 8, 15, 22, 7, 40, 11]:
    if i % 2 == 0:
        print(i)