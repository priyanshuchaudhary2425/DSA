# USING RECURSSION
def binarySearch(arr, target, low, high):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return binarySearch(arr, target, low, mid-1)

    elif arr[mid] < target:
        return binarySearch(arr, target, mid+1, high)

myarr = [1, 2, 3,4 ,5 ,6 ,7 , 8]

result = binarySearch(myarr, 5, 0, len(myarr) - 1)
print(result)


# WITHOUT RECURSION

def binarSearchSimple(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            high = mid - 1

        elif arr[mid] < target:
            low = mid + 1

    return -1

print(binarSearchSimple(myarr, 50))