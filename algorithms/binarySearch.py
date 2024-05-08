# Algorithm - Binary Search

# Works off of a sorted list
# Time Complexity: O(log n)
# Space Complexity: O(1)
# For each iteration, you divide your search space by 2
## iteration k = n / 2^k
from util import timeIt

@timeIt
def linearSearch(nums, target):
    # time complexity O(n)
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

@timeIt
def binarySearch(nums, target):
    # time complexity O(log n)
    leftIndex = 0
    rightIndex = len(nums) - 1
    middleIndex = 0

    while leftIndex <= rightIndex:
        middleIndex = (leftIndex + rightIndex) // 2
        middleNum = nums[middleIndex]

        if middleNum == target:
            return middleIndex
        
        if middleNum < target:
            leftIndex = middleIndex + 1
        else:
            rightIndex = middleIndex - 1

    return -1

def binarySearchRecursion(nums, target, leftIndex, rightIndex):
    if rightIndex < leftIndex:
        return -1 
    
    middleIndex = (leftIndex + rightIndex) // 2
    if middleIndex >= len(nums) or middleIndex < 0:
        return -1
    middleNum = nums[middleIndex]

    if middleNum == target:
        return middleIndex
    
    if middleNum < target:
        leftIndex = middleIndex + 1
    else:
        rightIndex = middleIndex - 1
    
    return binarySearchRecursion(nums, target, leftIndex, rightIndex)


if __name__ == '__main__':
    nums = [7, 13, 15, 26, 29, 40, 44, 50, 80, 83, 92]

    numsList = [i for i in range(1000000)] # for testing performance

    index1 = linearSearch(nums, 50)
    index2 = binarySearch(nums, 50)
    print(f"Index of target: {index1}")

    index3 = linearSearch(numsList, 8393820)
    index4 = binarySearch(numsList, 8393820)

    index5 = binarySearchRecursion(nums, 26, 0, len(nums) - 1)
    print(f"Index of target: {index5}")