def fibonacci(n):
    if type(n)!=int:
        return "Введено не число"
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    print(*fibonacci(10))