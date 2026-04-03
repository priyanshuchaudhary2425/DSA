def delete(array: list, index: int):
    if (index>=0 and index < len(array)):
        x = array[index]

        for i in range(index, len(array)-1):
            array[i] = array[i+1]
        size = len(array) - 1
        
    return array, size

arraylist = [1, 2, 3, 4, 5, 6]




def display(array: list, size: int):
    for i in range(size):
        print(array[i], end=" ")
    print()

result, size = delete(arraylist, 3)

display(result, size)