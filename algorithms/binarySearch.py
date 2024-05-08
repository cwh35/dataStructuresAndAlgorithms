# Algorithm - Binary Search

# Works off of a sorted list
# Time Complexity: O(log n)
# Space Complexity: O(1)
# For each iteration, you divide your search space by 2
## iteration k = n / 2^k

def linearSearch(nums, target):
    # time complexity O(n)
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

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


if __name__ == '__main__':
    nums = [7, 13, 15, 26, 29, 40, 44, 50, 80, 83, 92]

    index = binarySearch(nums, 50)
    print(f"Index of target: {index}")