def bubbleSort(elements, key):
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j][key] > elements[j + 1][key]:
                # swap
                temp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = temp
                swapped = True
                
        if not swapped:
            break

if __name__ == '__main__':
    elements = [
        { 'name': 'cam',   'transaction_amount': 5000, 'device': 'iphone-10'},
        { 'name': 'matt', 'transaction_amount': 500,  'device': 'google pixel'},
        { 'name': 'christian',  'transaction_amount': 150,  'device': 'vivo'},
        { 'name': 'cole',  'transaction_amount': 8900,  'device': 'iphone-8'},
    ]

    bubbleSort(elements, 'transaction_amount')
    print(elements)
    bubbleSort(elements, 'name')
    print(elements)