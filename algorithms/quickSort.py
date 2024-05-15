# Algorithm - Quick Sort

# works by using a pivot element
# divide and conquer problem
# putting a pivot in its correct positioning is partitioning
# two partitioning schemes:

## Hoare Partitioning
# --------------------
### pivot is first element, second element is starting pointer, last element is ending pointer
### move starting pointer until element is greater than pivot
### move ending pointer until element is less than pivot
### swap starting and ending values, then repeat the process
### when pointers cross, swap pivot with ending pointer

## Lomuto Partitioning
# --------------------
### pivot is last element
### starting element is first element, called p index (partition index)
### move p index until element is greater than pivot
### start another counter called i (i has same index as p index initially), move i until element is less than pivot
### swap i and p index, then increment p index, repeat the process

# average time complexity: O(nlogn)
# worst time complexity: O(n^2)
def swap(a, b, arr):
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp


def partition(elements, start, end):
    pivotIndex = start
    pivot = elements[pivotIndex]

    start = pivotIndex + 1
    end = len(elements) - 1

    while start < end: # do this until start and end pointers cross
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivotIndex, end, elements) # swap pivot with end pointer

    return end

def quickSort(elements, start, end):
    if start < end:
        partIndex = partition(elements, start, end)
        quickSort(elements, start, partIndex - 1) # left partition
        quickSort(elements, partIndex + 1, end) # right partition

if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    quickSort(elements, 0, len(elements) - 1)
    print(elements)