
# 1) nums = [1, 4, 6, 9, 10, 5, 7]

# this returns a -1 index because the list is not sorted

# 2) Find index of all occurances of a number from sorted list
def binarySearch(nums, target):
    # time complexity O(log n)
    leftIndex = 0
    rightIndex = len(nums) - 1
    middleIndex = 0
    indexList = []

    while leftIndex <= rightIndex:
        middleIndex = (leftIndex + rightIndex) // 2
        middleNum = nums[middleIndex]

        if middleNum == target:
            leftIndex = middleIndex - 1
            rightIndex = middleIndex + 1
            while nums[leftIndex] == target:
                indexList.append(leftIndex)
                leftIndex -= 1
            while nums[rightIndex] == target:
                indexList.append(rightIndex)
                rightIndex += 1
            
            indexList.append(middleIndex)
            indexList.sort()
            return indexList
        
        if middleNum < target:
            leftIndex = middleIndex + 1
        else:
            rightIndex = middleIndex - 1

    return -1

numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
numToFind = 15
numToFind2 = 34

print(binarySearch(numbers, numToFind))
print(binarySearch(numbers, numToFind2))

