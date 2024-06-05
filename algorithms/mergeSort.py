# Algorithm - Merge Sort

# divide and conquer problem
# divide the array into two halves, and keep doing it until the array is of size 1
# then merge the two halves back together, sorting them in the process

# time complexity: O(n log n)

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    # keep dividing arrays until length is 1
    left = mergeSort(left)
    right = mergeSort(right)

    return mergeTwoSortedLists(left, right)

def mergeTwoSortedLists(a, b):
    sortedList = []
    lenA = len(a)
    lenB = len(b)

    i = j = 0

    while i < lenA and j < lenB:
        if a[i] < b[j]:
            sortedList.append(a[i])
            i += 1
        else:
            sortedList.append(b[j])
            j += 1
    while i < lenA:
        sortedList.append(a[i])
        i += 1
    while j < lenB:
        sortedList.append(b[j])
        j += 1
    
    return sortedList

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]

    print("Given array is", arr)
    print(mergeSort(arr))