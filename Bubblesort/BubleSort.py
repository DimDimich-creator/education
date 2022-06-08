Myarray = input('Введите числа через пробел: ').split()
Myarray = [int(item) for item in Myarray]


def BubbleSort(array):
    for k in range(1, len(array)):
        for i in range(len(array) - k):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array


print(BubbleSort(Myarray))
