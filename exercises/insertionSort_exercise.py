def insertionSort(elements):
    medians = []  # List to store the medians
    for i in range(1, len(elements)):
        anchor = elements[i]  # Element we are dealing with in the unsorted array
        j = i - 1  # Pointer to the sorted array
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = anchor
        sorted_array = elements[:i+1]  # Get the sorted array so far
        if i % 2 == 0:
            median = sorted_array[i // 2]
        else:
            median = (sorted_array[i // 2] + sorted_array[i // 2 + 1]) / 2
        medians.append(median)  # Append the median to the list

    return medians

if __name__ == '__main__':
    elements = [2, 1, 5, 7, 2, 0, 5]
    medians = insertionSort(elements)
    for median in medians:
        print(median)