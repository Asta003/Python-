# числовой int
age = 25
print(age)

# текстовый тип str
name = "Alice"
print(name)


# логический тип булен
Dima_is_student = True
print(Dima_is_student)

# последовательный тип list
fruits = ["apple", "banana", "orange"]
print(fruits)

# типы множеств set 
numbers = {1, 2, 3, 3, 4}
print(numbers)

# двоичный тип bytes
data = b"Hello"
print(data)

# спец тип NoneType
nothing = None
print(nothing)





# Арифметические операторы

# Сложение
print(5 + 3)

# Вычитание
print(10 - 4)

# Умножение
print(6 * 7) 

# Деление
print(15 / 4)     

# Целочисленное деление
print(15 // 4)  

# Остаток от деления
print(17 % 5)  

# Возведение в степень
print(2 ** 4)  




# Операторы сравнения 

x, y = 10, 5

print(x == y)    #(равно)
print(x != y)    #(не равно)
print(x > y)     #(больше)
print(x < y)     #(меньше)
print(x >= y)    #(больше или равно)
print(x <= y)    #(меньше или равно)




# Логические операторы

a, b = True, False

print(a and b) 
print(a or b)    
print(not a)  


# Операторы присваивания

# Простое присваивание
x = 10
print(x)        

# Сложение с присваиванием
x += 5         
print(x)         

# Вычитание с присваиванием
x -= 3           
print(x)        

# Умножение с присваиванием
x *= 2           
print(x)        

# Деление с присваиванием
x /= 4           
print(x)         

# Целочисленное деление с присваиванием
x //= 2          
print(x)         

# Остаток от деления с присваиванием
x %= 2          
print(x)         

# Возведение в степень с присваиванием
x **= 3          
print(x)     


# Операторы принадлежности

fruits = ["apple", "banana", "orange"]

print("apple" in fruits)       
print("grape" not in fruits)    

text = "Hello World"
print("Hello" in text)          
print("Python" not in text)     


# Битовые операторы
z = 2
v = 3

print(z & v) #и

print(z | v) #или

print(z ^ v) #или нет

print(~-v) #инвертация

print(z << v) #сдвиг влево

print(z >> v) #сдвиг вправо