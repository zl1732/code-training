# 到底要给 mid 加一还是减一，while 里到底用 <= 还是 <。
# 最常用的二分查找场景：寻找一个数、寻找左侧边界、寻找右侧边界。


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

"""
分析二分查找的技巧是：
    1. 不要出现 else，而是把所有情况用 else if 写清楚，这样可以清楚地展现所有细节。

    2. 计算 mid 时需要防止溢出，代码中 left + (right - left) / 2 就和 (left + right) / 2 的结果相同，但是有效防止了 left 和 right 太大，直接相加导致溢出的情况。
"""


# 一、寻找一个数（基本的二分搜索）
def search(nums, target):
    left = 0
    # 注意
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # 注意
            left = mid + 1
        elif nums[mid] > target:
            # 注意
            right = mid - 1
    return -1

"""
1. 为什么 while 循环的条件是 <= 而不是 <？


    因为初始化 right 的赋值是 nums.length - 1，即最后一个元素的索引，而不是 nums.length。
        前者相当于两端都闭区间 [left, right]，后者相当于左闭右开区间 [left, right)
        我们这个算法中使用的是前者 [left, right] 两端都闭的区间。这个区间其实就是每次进行搜索的区间。

        方式1:
        while(left <= right) 的终止条件是 left == right + 1，
            写成区间的形式就是 [right + 1, right]，或者带个具体的数字进去 [3, 2]，可见这时候区间为空。
            所以这时候 while 循环终止是正确的，直接返回 -1 即可。

        方式2:
        while(left < right) 的终止条件是 left == right，
            写成区间的形式就是 [right, right]，或者带个具体的数字进去 [2, 2]，这时候区间非空，还有一个数 2，
            但此时 while 循环终止了。也就是说区间 [2, 2] 被漏掉了，索引 2 没有被搜索，如果这时候直接返回 -1 就是错误的。
        
            如果一定要这么写，需要打补丁：
            # ...
            while left < right:
                # ...
            return left if nums[left] == target else -1

            
2. 为什么是 left = mid + 1，right = mid - 1？

    刚才明确了「搜索区间」这个概念，而且本算法的搜索区间是两端都闭的，即 [left, right]。
    那么当我们发现索引 mid 不是要找的 target 时，下一步应该去搜索哪里呢？
        当然是去搜索区间 [left, mid-1] 或者区间 [mid+1, right] 因为 mid 已经搜索过，应该从搜索区间中去除。

    缺陷：
    多个目标数存在，无法查找左右边界
        比如说给你有序数组 nums = [1,2,2,2,3]，target 为 2，无法查找 左边界 1 和 右边界 3
        找到一个 target，然后向左或向右线性搜索？难以保证二分查找对数级的复杂度了。


"""


# 二、寻找左侧边界的二分搜索
def left_bound(nums: List[int], target: int) -> int:
    left = 0
    # 注意
    right = len(nums)
    
    # 注意
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            # 注意
            right = mid

    return left

"""
1. 为什么 while 中是 < 而不是 <=？
    因为 right = nums.length 而不是 nums.length - 1。因此每次循环的「搜索区间」是 [left, right) 左闭右开。
    while(left < right) 终止的条件是 left == right，此时搜索区间 [left, left) 为空，所以可以正确终止。

2. target 不存在时返回什么？
    如果 target 不存在，搜索左侧边界的二分搜索返回的索引是大于 target 的最小索引。
    int floor(int[] nums, int target) {
        // 当 target 不存在，比如输入 [4,6,8,10], target = 7
        // left_bound 返回 2，减一就是 1，元素 6 就是小于 7 的最大元素
        // 当 target 存在，比如输入 [4,6,8,8,8,10], target = 8
        // left_bound 返回 2，减一就是 1，元素 6 就是小于 8 的最大元素
        return left_bound(nums, target) - 1;
    }

    如果想让 target 不存在时返回 -1 返回的时候额外判断一下 nums[left] 是否等于 target 就行了，如果不等于，就说明 target 不存在。

    
3. 为什么是 left = mid + 1 和 right = mid？
    因为我们的「搜索区间」是 [left, right) 左闭右开，
    所以当 nums[mid] 被检测之后，下一步应该去 mid 的左侧或者右侧区间搜索，
    即 [left, mid) 或 [mid + 1, right)。

4. 为什么该算法能够搜索左侧边界？
    关键在于对于 nums[mid] == target 这种情况的处理：
        if (nums[mid] == target)
            right = mid;
    可见，找到 target 时不要立即返回，而是缩小「搜索区间」的上界 right，在区间 [left, mid) 中继续搜索，即不断向左收缩，达到锁定左侧边界的目的。

    
5. 为什么返回 left 而不是 right？
    答：都是一样的，因为 while 终止的条件是 left == right。

6. 能否统一成两端都闭的搜索区间？

"""

def left_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    # 搜索区间为 [left, right]
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            # 搜索区间变为 [mid+1, right]
            left = mid + 1
        elif nums[mid] > target:
            # 搜索区间变为 [left, mid-1]
            right = mid - 1
        elif nums[mid] == target:
            # 收缩右侧边界
            right = mid - 1
    
    # 判断 target 是否存在于 nums 中
    # 如果越界，target 肯定不存在，返回 -1
    if left < 0 or left >= len(nums):
        return -1
    
    # 判断一下 nums[left] 是不是 target
    return left if nums[left] == target else -1




# 三、寻找右侧边界的二分查找
def right_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            # 注意
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    # 注意
    return left - 1

"""
如果 target 不存在，搜索右侧边界的二分搜索返回的索引是小于 target 的最大索引。
"""

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
    # 最后改成返回 left - 1
    if left - 1 < 0 or left - 1 >= len(nums):
        return -1
    return left - 1 if nums[left - 1] == target else -1



# 第一个，最基本的二分查找算法：
# 因为我们初始化 right = nums.length - 1
# 所以决定了我们的「搜索区间」是 [left, right]
# 所以决定了 while (left <= right)
# 同时也决定了 left = mid+1 和 right = mid-1

# 因为我们只需找到一个 target 的索引即可
# 所以当 nums[mid] == target 时可以立即返回


# 第二个，寻找左侧边界的二分查找：


# 因为我们初始化 right = nums.length
# 所以决定了我们的「搜索区间」是 [left, right)
# 所以决定了 while (left < right)
# 同时也决定了 left = mid + 1 和 right = mid

# 因为我们需找到 target 的最左侧索引
# 所以当 nums[mid] == target 时不要立即返回
# 而要收紧右侧边界以锁定左侧边界



# 第三个，寻找右侧边界的二分查找：


# 因为我们初始化 right = nums.length
# 所以决定了我们的「搜索区间」是 [left, right)
# 所以决定了 while (left < right)
# 同时也决定了 left = mid + 1 和 right = mid

# 因为我们需找到 target 的最右侧索引
# 所以当 nums[mid] == target 时不要立即返回
# 而要收紧左侧边界以锁定右侧边界

# 又因为收紧左侧边界时必须 left = mid + 1
# 所以最后无论返回 left 还是 right，必须减一