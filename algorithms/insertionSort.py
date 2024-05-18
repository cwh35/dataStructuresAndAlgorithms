# Algorithm - Insertion Sort

# create a second array - sorted array
# take element from unsorted array and put it into sorted array
# ex: [21, 38, 29, 17, 4, 25, 11, 32, 9]
# sorted array: [21] unsorted array: [38, 29, 17, 4, 25, 11, 32, 9]
# sorted array: [21, 38] unsorted array: [29, 17, 4, 25, 11, 32, 9]
# sorted array: [21, 29, 38] unsorted array: [17, 4, 25, 11, 32, 9]

# this uses a second array, can we use this without using an extra array?

# single array approach
# take a pointer, start from second element
# anything to the left of pointer is the sorted array
# move the pointer to the right, compare the element with the sorted array
# start with the right most part of the sorted array, and move a pointer until you find the spot where
## the unsorted element is greater than the sorted element

## performance
## -----------
# worst-case: O(n^2) comparisons & swaps
# best-case: O(n) comparisons, O(1) swaps
# avg-case: O(n^2) comparisons & swaps
# worst-case space: O(n) total, O(1) auxillary

def insertionSort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i] # element we are dealing with in the unsorted array
        j = i - 1 # pointer to the sorted array
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = anchor

if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    insertionSort(elements)
    print(elements)