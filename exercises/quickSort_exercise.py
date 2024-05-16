# Exercise using quick sort by implementing the Lomuto partitioning scheme

def swap(a, b, arr):
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

def quickSort(arr, start, end):
    if len(elements) == 1:
        return
    if start < end:
        partIndex = partition(arr, start, end)
        quickSort(arr, start, partIndex - 1)
        quickSort(arr, partIndex + 1, end)

def partition(arr, start, end):
    pivot = arr[end]
    pIndex = start

    for i in range(start, end):
        # if current element is less than or equal to pivot
        if arr[i] <= pivot:
            swap(i, pIndex, arr)
            # increment temporary pivot index
            pIndex += 1
    # swap pivot with last element
    swap(pIndex, end, arr)

    return pIndex

if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    quickSort(elements, 0, len(elements) - 1)
    print(elements)