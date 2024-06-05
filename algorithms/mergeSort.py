# Algorithm - Merge Sort

# divide and conquer problem
# divide the array into two halves, and keep doing it until the array is of size 1
# then merge the two halves back together, sorting them in the process

# time complexity: O(n log n)

def mergeSort(arr):
    if len(arr) <= 1:
        return
    
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    # keep dividing arrays until length is 1
    mergeSort(left)
    mergeSort(right)

    return mergeTwoSortedLists(left, right, arr)

def mergeTwoSortedLists(a, b, arr):
    sortedList = []
    lenA = len(a)
    lenB = len(b)

    i = j = k = 0
    # k is index of sorted array "arr"

    while i < lenA and j < lenB:
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < lenA:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < lenB:
        arr[k] = b[j]
        j += 1
        k += 1
    
    return sortedList

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]

    mergeSort(arr)
    print(arr)