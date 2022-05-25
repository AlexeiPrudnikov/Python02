def Sequence(n):
    result = []
    if n < 1: return result
    for i in range(1, n + 1):
        result.append((1 + 1/i)** i)
    return result
def SummList(items):
    summ = 0
    for i in items:
        summ += i
    return summ
try:
    n = int(input('Введите число N: '))
    sequence = Sequence(n)
    print('Последовательность...')
    print(sequence)
    print(f'Сумма последовательности при n = {n} равна {SummList(sequence)}')
except ValueError:
    print('Введено не число')


