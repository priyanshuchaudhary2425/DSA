def Get(arr, ind):
    if 0 <= ind <= (len(arr) - 1):
        return arr[ind]

arrLi = [1, 2, 3, 4, 5, 6, 7, 8]

result = Get(arrLi, 7)
print(result)

def SET(arr, ind, value):

    if 0 <= ind <= (len(arr) - 1):
        arr[ind] = value
        return arr


SETRESULT = SET(arrLi, 2, 100)
print(SETRESULT)

def MAX(arr):

    value = arr[0]

    for i in arr:
        if i > value:
            value = i

    return value


MAXRESULT = MAX(arrLi)
print(MAXRESULT)