def reverseArray(arr):
    i = 0
    j = (len(arr) - 1)

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr

def reverseArray2(arr):
    b = []

    for i in range(len(arr) - 1, -1, -1):
        b.append(arr[i])

    for i in range(len(b)):
        arr[i] = b[i]

    return arr


def reverseArray3(arr):
    j = len(arr) - 1

    for i in range(len(arr)):
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    return arr


arrList = [1, 2, 3, 4, 5]
arrList2 = [9, 10, 11, 12]
arrList3 = [100, 99, 98, 97, 96]

print(reverseArray(arrList))
print(reverseArray2(arrList2))
print(reverseArray3(arrList3))

print(arrList3)
