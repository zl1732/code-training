# 二分查找框架
def binarySearch(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while ...:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            ...
        elif nums[mid] < target:
            left = ...
        elif nums[mid] > target:
            right = ...
    return ...


# 一、寻找一个数（基本的二分搜索）
def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1


# 二、寻找左侧边界的二分搜索
def left_bound(nums: List[int], target: int) -> int:
    # 右侧开区间
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    if left >= len(nums):
        return -1
    return left if nums[left] == target else -1


def left_bound(nums: List[int], target: int) -> int:
    # 右侧闭区间
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            right = mid - 1
    if left >= len(nums):
        return -1
    return left if nums[left] == target else -1




# 三、寻找右侧边界的二分查找
def right_bound(nums, target):
    # 右侧开区间
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right-left)// 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid +1
    if left-1 < 0:
        return -1
    return left-1 if nums[left-1] != target else -1
""" 右侧开区间，target<所有数，left = right = 0，注意这里right=0代表[0,0)]
    也就是取不到这个区间， left其实是-1
"""

def right_bound(nums, target):
    # 右侧闭区间
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right-left)// 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid-1
        elif nums[mid] < target:
            left = mid +1
    # if right < 0:
    #     return -1
    # return right if nums[right] != target
    if left-1 < 0:
        return -1
    return left-1 if nums[left-1] != target else -1
""" 右侧闭区间，target<所有数，left=0, right = -1，注意这里right=0代表[0,-1]]
"""

开区间
| 变量     | 最小值 | 最大值        |
| ------- | ----- | ------------- |
| `left`  | 0     | `len(nums)`   | 
| `right` | 0     | `len(nums)`   | 


闭区间
| 变量     | 最小值 | 最大值        |
| ------- | ----- | ------------- |
| `left`  | 0     | `len(nums)`   | 
| `right` | `-1`  | `len(nums)-1` |


#统一使用闭区间：
def left_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            right = mid - 1
    if left < 0 or left >= len(nums): #if left >= len(nums):
        return -1
    return left if nums[left] == target else -1

def right_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            left = mid + 1
    if right < 0 or right >= len(nums): # if right < 0:
        return -1
    return right if nums[right] == target else -1



