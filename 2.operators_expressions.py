x = 10
y = 8
# Арифметические
print(x + y)  # Сложение
print(x - y)  # Вычитание
print(x / y)  # Деление
print(x * y)  # Умножение
print(x % y)  # Остаток от деления
print(x ** y)  # Возведение в степень

# Приоритет операций
print((x + y) * y)  # То что в скобках
print(x ** y + x)  # 2 степень
print(x * y / y + x)  # 3 Умножение и деление
print(x + y - x)  # 4 Сложение и вычитание

b = 5
a = 2

# Присваивание
b += a
print(b)

print(b < a)
print(b > a)
print(not (b == a))
