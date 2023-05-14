# переменные, операторы, условные операторы, циклы и функции.
# Переменная в Python - это именованное место в памяти, которое используется для хранения данных.
# Для определения переменной в Python используется оператор присваивания "=".
# x = 5  # создание переменной "x" со занчением 5
# y = "Hello, World!"  # creating a variable "y" with a valve "Hello, world"


# Операторы в Python используются для выполнения различных операций над переменными и значениями.

# Арифметические операторы/arithmetic operators
x = 5
y = 3
print(x + y)  # Сложение/Summation
print(x - y)  # Вычетание/Subtraction
print(x * y)  # Умножение/Multiplication
print(x / y)  # Деление/Dividing
print(x % y)  # Остаток от деления/The remainder fo the division
print(x ** y)  # Возведение в степень/The exponentiation

# Операторы сравнения/Comparison operators
x = 5
y = 3
print(x == y)  # Равно/equal (результат: False)
print(x != y)  # Не равно/Not equal (result: True)
print(x > y)  # Больше/Greater than (result: True)
print(x < y)  # Меньше/Less than (result: False)
print(x >= y)  # Больше или равно/Greater then or equal to (result: True)
print(x <= y)  # Меньше или равно/Less then or equal to (result: False)

# Логические опператоры/logical operators
x = True
y = False
print(x and y)  # И/and (false)
print(x or y)  # Или/Or (True)
print(not x)  # Не/Not (False)

# Условные операторы/Conditional operators
# Оператор if
x = 5
if x > 0:
    print("x больше 0")
# Оператор if-else
x = 5
if x > 0:
    print("x больше 0")
else:
    print("x меньше или равно 0")
# Оператор if-elif-else
x = 5
if x > 0:
    print("x больше 0")
elif x == 0:
    print("x равно 0")
else:
    print("x меньше 0")

# Циклы/cycles
# Цикл while
x = 0
while x < 5:
    print(x)
    x += 1
# Цикл for
colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)


# Функции
# Определение функции
def greet(name):
    print("Hello, " + name + "!")


# Вызов функции
greet("Gleb")
greet("Vera")
greet("Boris")
greet("Katya")


def square(u):
    return u * u


result = square(5)
print(result)


def add_numbers(j, h=0):
    return j + h

# проверка
