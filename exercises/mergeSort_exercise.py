# Modify the merge sort function so that it can sort the following list of athletes
# based on their time taken by them in the marathon

def mergeSort(arr, key='name', descending=False):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    # keep dividing arrays until length is 1
    left = mergeSort(left, key, descending)
    right = mergeSort(right, key, descending)
    sortedList = mergeTwoSortedLists(left, right, key, descending)

    return sortedList

def mergeTwoSortedLists(left, right, key, descending=False):
    merged = []
    
    if descending:
        while len(left) > 0 and len(right) > 0:
            if left[0][key] >= right[0][key]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
    else:
        while len(left) > 0 and len(right) > 0:
            if left[0][key] <= right[0][key]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
    
    merged.extend(left)
    merged.extend(right)

    return merged
        

if __name__ == '__main__':
    elements = [
        { 'name': 'cameron', 'age': 22, 'time_in_hours': 1},
        { 'name': 'matt', 'age': 23, 'time_in_hours': 3},
        { 'name': 'christian', 'age': 25, 'time_in_hours': 2.5},
        { 'name': 'cole', 'age': 31, 'time_in_hours': 1.5},
    ]

    sortedList = mergeSort(elements, key="time_in_hours", descending=False)
    print(sortedList)
    sortedList = mergeSort(elements, key="time_in_hours", descending=True)
    print(sortedList)
    sortedList = mergeSort(elements, key='name')
    print(sortedList)
