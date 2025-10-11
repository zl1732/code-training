
# 滑动窗口 1658
"""
11 12 9993 0
12 13 9904 0
13 14 8819 0
14 15 1231 0
15 16 6309 0

下面这个方法的问题在于：
最后一轮 走到 15 16，left += 1执行完，
while left < right不会再执行了，但是其实16 16这一轮才是解

"""

def minOperations(nums, x) -> int:
    # 用 window 记sum
    window = 0
    target = sum(nums) - x
    max_len = -1
    left = right = 0 
    
    while right < len(nums):
        num = nums[right]
        right += 1
        window += num
        while left < right and window >= target:
            # print(left, right,window, target)
            if window == target:
                max_len = max(max_len,right - left)
            # 左移动
            num = nums[left]
            window -= num
            left += 1
    return -1 if max_len == -1 else len(nums) - max_len

nums = [8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309]
x = 134365
minOperations(nums, x)


def minOperations2(nums, x) -> int:
    # 用 window 记sum
    window = 0
    target = sum(nums) - x
    max_len = float('-inf')
    left = right = 0 
    
    while right < len(nums):
        num = nums[right]
        right += 1
        window += num
        while left < right and window > target:
            print(left, right,window, target)
            
            # 左移动
            num = nums[left]
            window -= num
            left += 1
            print(left, right,window, target)


        # if window == target:
        #     max_len = max(max_len,right - left)
            if window == target:
                max_len = max(max_len,right - left)

    return -1 if max_len == float('-inf') else len(nums) - max_len
minOperations2(nums, x)



s = "8264"
number = 0
for i in range(len(s)):
    # 将字符转化成数字
    number = 10 * number + (ord(s[i]) - ord('0'))
    print(number)

print(ord('8') - ord('0'))



from typing import List
def left_bound(nums: List[int], target: int) -> int:
    left = 0
    # 注意
    right = len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    print(left, right)
nums = [2,2,2,2,3]
target = 2
# target = 4
left_bound(nums, target)
# 左边界，开区间 0, 0


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
    print(left, right)

nums = [2,2,2,2,3]
target = 2
# target = 4
left_bound(nums, target)
# 左边界，闭区间 0, -1


# 三、寻找右侧边界的二分查找
def right_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    print(left, right)
    return left - 1
nums = [1,2,2,2,2]
target = 2
target = 0
target = 3
right_bound(nums, target)
# 右边界，开区间 5, 5




def right_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # 这里改成收缩左侧边界即可
            left = mid + 1
    print(left, right)
    return right
nums = [1,2,2,2,2]
target = 2
target = 0
target = 3
right_bound(nums, target)
# 右边界，闭区间 5, 4

print("*"*50)

from collections import defaultdict
def numMatchingSubseq( s: str, words: List[str]) -> int:
    # 建立查询矩阵
    lookup = defaultdict(list)

    for i, char in enumerate(s):
        if char not in lookup:
            lookup[char] = [-1, i]
        else:
            # 增加占位符
            lookup[char].append(i)
    
    # loop 
    res = 0
    for word in words:
        # bbb abcabcb 
        i = j = 0
        while i < len(word) and j < len(s):
            search_ch = word[i]
            nums = lookup[search_ch]  #[-1, 1 4 6]
            target = j
            
            # 二分查找
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            if left+1 == len(nums):
                break
            
            # 找到了当前位,bbb下一位，abcabcb移动到找到的位置left的index
            i += 1
            j = nums[left] if nums[mid] == target else nums[left + 1]
        print(word, i , j)

            
        if i + 1 == len(word):
            res += 1
        print(res)
    return res

s = "abcabcb"
s = "abcde"
words = ["bbb"]
words = ["acd","ace"]
numMatchingSubseq(s, words)