Myarray = input('Введите числа через пробел: ').split()
Myarray = [int(item) for item in Myarray]


def MargSort(array):
    if len(array) == 1 or len(array) == 0:
        return array
    D = MargSort(array[(len(array)//2):(len(array))])
    C = MargSort(array[0:(len(array)//2)])
    i, j, B = 0, 0, []
    while len(D) > j and len(C) > i:
        if D[j] > C[i]:
            B += [C[i]]
            i += 1
        else:
            B += [D[j]]
            j += 1
    while len(D) > j:
        B += [D[j]]
        j += 1
    while len(C) > i:
        B += [C[i]]
        i += 1
    return B


print(*MargSort(Myarray))
