# Создание функции
def fibonacchi(limit):
    a = 0
    b = 1
    fib = []
    while a < limit:
        a, b = b, a + b
        fib.append(a)
    return fib


if __name__ == '__main__':
    result = fibonacchi(2000)
    print(result)


def factorial(num):
    result = 1
    if num < 0:
        print("Число должно быть меньше 0!")
    elif num == 1 or num == 0:
        return 1
    else:
        for i in range(2, num + 1):
            result = result * i
    return result


if __name__ == '__main__':
    result = factorial(6)
    print(result)
