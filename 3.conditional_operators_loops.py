x = 8
y = 17
c = (y / x)
if isinstance((c), int):  # Приводим к целому числу, деление всегда приводит чилсо к float
    print(int(c))
elif isinstance(c, float):
    print("{:.2f}".format(c))
else:
    print("Error")

# Цикл while
x = 0
while x < 5:
    print(x)
    x += 1

#
