# Algorithm - Bubble Sort 

# begin sorting by comparing first two elements
## ex. [38, 9, 29, 7, 2, 15, 28]
## if 38 > 9, swap
# biggest number will bubble up to the end of the list
# repeat until no swaps are made

# Time Complexity: O(n^2)
# Space Complexity: O(1) - not using any extra space, using the same array
def bubbleSort(elements):
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                # swap
                temp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = temp
                swapped = True
                
        if not swapped:
            break

if __name__ == '__main__':
    elements = [5, 9, 2, 1, 67, 34, 88, 34]

    bubbleSort(elements)
    print(elements)