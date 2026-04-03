def linearSearch(array:list, target):
    for i, val in enumerate(array):
        if val == target:
            array[0], array[i] = array[i], array[0]
            return 0
    return -1




demoarray = [1, 2, 3, 4, 5, 6]

result = linearSearch(array=demoarray, target=6)
print(result)
print(demoarray)