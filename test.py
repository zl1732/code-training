
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

print("*"*50)

def lengthLongestPath(input: str) -> int:
    st = []
    max_len = 0
    # line
    paths = input.split('\n')
    for path in paths:
        level = path.rfind('\t') + 1
        print(level, path)
        while st and level < len(st):
            st.pop()
        """
        append 要减去 level，否则后面多个path会多次加level
        """
        st.append(len(path)-level)
        # 如果是文件，就计算路径长度
        if "." in path:
            l = sum(st) + len(st) - 1
            # 加上父路径的分隔符
            max_len = max(max_len, l)
            print(max_len)
    return max_len

s = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
lengthLongestPath(s)



print("*"*50)


def next_greater_debug_visual(nums):
    n = len(nums)
    res = [-1] * n
    st = []  # 存索引，保持递减（栈顶最小）

    def draw_stack(stack):
        """打印栈内容的可视化小图"""
        if not stack:
            print("  [栈为空]")
            return
        # 找最大高度用于缩放
        maxh = max(nums[i] for i in stack)
        print("  栈结构：")
        for h in range(maxh, 0, -1):
            line = ""
            for i in stack:
                line += "  █ " if nums[i] >= h else "    "
            print(line)
        print(" ", " ".join(f"{nums[i]:2d}" for i in stack))
        print("  ↑↑ 栈底 → 栈顶 ↑↑")

    print(f"\nnums = {nums}")
    print("初始状态: res =", res)
    print("=" * 60)

    for i in range(n):
        print(f"🔹 当前元素: i={i}, nums[i]={nums[i]}")
        while st and nums[i] > nums[st[-1]]:
            idx = st.pop()
            res[idx] = nums[i]
            print(f"  ⚙️ nums[{i}]={nums[i]} > nums[{idx}]={nums[idx]} → 弹出 idx={idx}, res[{idx}]={nums[i]}")
            draw_stack(st)
            print("-" * 40)
        st.append(i)
        print(f"  ➕ 入栈 i={i}, 当前栈索引={st}")
        draw_stack(st)
        print(f"  📊 当前 res = {res}")
        print("=" * 60)

    print(f"✅ 最终结果: {res}\n")
    return res



# # 1️⃣ 基本例子：常规混合序列
# next_greater_debug([2, 1, 2, 4, 3])

# # 2️⃣ 全递减序列：最坏情况（所有元素都入栈）
# next_greater_debug([9, 8, 7, 6, 5])

# # 3️⃣ 全递增序列：最顺畅情况（每次都立刻弹栈）
# next_greater_debug([1, 2, 3, 4, 5])

# # 4️⃣ 波浪序列：多次触发 while
# next_greater_debug([2, 5, 1, 3, 4])

# # 5️⃣ 极端情况：全相等
# next_greater_debug([3, 3, 3, 3])


# st = []
# print(st[-1])



class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = self.nextGreaterElement_helper1(nums2)
        greater_map = {}
        for i, num in enumerate(nums2):
            # 正序
            greater_map[num] = greater[i]
        res = [greater_map[i] for i in nums1]

        # greater = self.nextGreaterElement_helper2(nums2)
        # greater_map = {}
        # for i, num in enumerate(nums2):
        #     # 反序
        #     greater_map[num] = greater[num]
        # res = [greater_map[i] for i in nums1]
        return res


    def nextGreaterElement_helper1(self, nums):
        # 正序
        st = []
        res = [-1] * len(nums)
        for i, cur in enumerate(nums):
            while st and cur > nums[st[-1]]:
                idx = st.pop()
                res[idx] = cur
            st.append(i)
        return res

    def nextGreaterElement_helper2(self, nums):
        # 反序
        st = []
        n = len(nums)
        res = [-1] * n
        for i in range(n-1, -1, -1):
            cur = nums[i]
            while st and cur >= st[-1]:
                st.pop()
            res[i] = -1 if not st else st[-1]
            st.append(cur)
        return res
nums1 = [4,1,2]
nums2 = [1,3,4,2]
a=  Solution()
a.nextGreaterElement(nums1, nums2)


print("*"*50)

times =  [2,6,4,8,10,9,15]
res = 0
max_time = 0
n = len(times)
for i in range(n - 1, -1, -1):
    print()
    print(times)
    print("num:", times[i])
    print('_'*20)
    if times[i] > max_time:
        max_time = times[i]
        res += 1
    print(max_time)




from collections import deque
def maxSubArray(nums):
    n = len(nums)
    preSum = [0] * (n + 1)
    for i in range(1, n + 1):
        preSum[i] = preSum[i - 1] + nums[i - 1]

    
    # 单调队列维护最小前缀和
    q = deque()
    q.append(0)
    res = float('-inf')

    for i in range(1, n + 1):
        print(i, preSum)
        print([preSum[i] for i in q])
        print(preSum[i], preSum[q[0]])
        res = max(res, preSum[i] - preSum[q[0]])
        # 保持队列递增（前缀和小的留着）
        while q and preSum[q[-1]] >= preSum[i]:
            q.pop()
        print(q)
        q.append(i)
        print('---------')
    return res

maxSubArray([-2,1,-3,4,-1,2,1,-5,4],)
