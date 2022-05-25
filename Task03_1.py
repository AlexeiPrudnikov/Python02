import random
minValue = -100
maxValue = 100
try:
    countElements = int(input('Введите длину последовательности: '))
    if countElements >= 0:
        print(f'Производится генерация последовательности длины {countElements}...')
        intList = []
        for i in range(countElements):
            intList.append(random.randint(minValue, maxValue))
        print(intList)
        random.shuffle(intList)
        print('Случайно перемешанная последовательность...')
        print(intList)
    else:
        print('Число элементов должно быть больше 0')
except ValueError:
    print('Введено не число')