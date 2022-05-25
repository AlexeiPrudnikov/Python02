def Factorial(n):
    result = []
    if n <= 0 : return result
    result.append(1)
    for i in range(2, n + 1):
        result.append(i * result[i - 2])
    return result
try:
    n = int(input('Введите число N: '))
    print(Factorial(n))
except ValueError:
    print('Введено не число')