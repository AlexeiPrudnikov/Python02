import random
minValue = -100
maxValue = 100
def randomIndex(n):
    listIndex = []
    while (len(listIndex) <= n-1):
        index = 0
        while (index >= 0):
            index = random.randint(0, n - 1)
            if index not in listIndex:
                listIndex.append(index)
                index = -1
    return listIndex
def randomSort(startList, indexList):
    resultList = []
    for i in indexList:
        resultList.append(startList[i])
    return resultList
try:
    countElements = int(input('Введите длину последовательности: '))
    if countElements >= 0:
        print(f'Производится генерация последовательности длины {countElements}...')
        intList = []
        for i in range(countElements):
            intList.append(random.randint(minValue, maxValue))
        print(intList)
        print('Случайно перемешанная последовательность...')
        print(randomSort(intList, randomIndex(countElements)))
    else:
        print('Число элементов должно быть больше 0')
except ValueError:
    print('Введено не число')