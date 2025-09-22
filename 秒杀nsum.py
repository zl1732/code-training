# two sum
class Solution:
    """
    标准普通写法
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()
        for i,num in enumerate(nums):
            if target-num in lookup:
                return [lookup[target-num], i]
            lookup[num] = i
        return []
        
    """
    双指针
    """
    """
    关于 twoSumTarget 里 if/elif/else 和 if/if/if 的区别：

    1. 常见写法是 if/elif/else
    - 三个条件互斥，只会命中其中一个分支
    - 语义清晰：要么 sum < target，要么 sum > target，要么 sum == target
    - 一次循环中最多只会移动 lo 或 hi，或者保存一次解

    2. 如果写成三个独立的 if
    - 条件依然互斥，所以实际上效果大部分时候是一样的
    - 当 sum == target 时，只会进入第三个 if，前两个 if 不会触发
    - 第三个 if 里有 while 去重逻辑：
            while lo < hi and nums[lo] == left: lo += 1
            while lo < hi and nums[hi] == right: hi -= 1
        → 这能保证重复的数被跳过，因此不会多次加入相同解

    ✅ 简短总结：
        三个 if 在严格互斥 (<, >, ==) 且不重算、不多挪指针时结果和 if/elif/else 一样。
        但可读性差，维护时很容易埋雷：一旦有人改成 <= / >=、本轮重算、双向挪指针，就可能导致 漏解 / 重复 / 越界。
        更推荐 if/elif/else 或者 if+continue，语义清晰、稳健，不容易出 bug。
    """
    # 如果没有重复，可能有多个解
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 先对数组排序
        nums.sort()
        res = []
        lo, hi = 0, len(nums)-1
        while lo<hi:
            sum = nums[lo] + nums[hi]
            if sum < target:
                lo += 1
            elif sum > target:
                hi -= 1
            else:
                res.append([lo, hi])
                lo += 1
                hi -= 1
        return res
    
    # ❌ 去重解法 ❌
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 先对数组排序
        nums.sort()
        res = []
        lo, hi = 0, len(nums)-1
        while lo<hi:
            sum = nums[lo] + nums[hi]
            cur_left = nums[lo]
            cur_right = nums[hi]
            """
            错误
            只有在sum<target的情况下才能继续找是否有重复
            """
            if sum < target or nums[lo] == cur_left:
                lo += 1
            elif sum > target or nums[hi] == cur_right:
                hi -= 1
            else:
                res.append([lo, hi])
                """
                关于为什么需要再次检验:
                [-2,0,.,0,2]
                    |   |
                    lo  hi
                nums = [-2, 0, .., 0, 2]
                target = 0
                流程：
                    外层取 -2
                    twoSumTarget 里：lo=1, hi=4
                    第一次：cur = 0+2=2 > 2 → hi--
                    再来：lo=1(0), hi=3(0) → cur=0 → 命中！
                    → 解是 [0,0]
                问题来了：nums[lo] 和 nums[hi] 中间还有很多 0，

                另外：
                为什么不要用lo+1, hi-1
                越界风险!!,不要自作聪明，lo<hi+1

                """
                while lo < hi and nums[lo + 1] == cur_left:
                    lo += 1
                while lo< hi and nums[hi - 1] == cur_right:
                    hi -= 1
        return res
    
    # 去重解法
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 先对数组排序
        nums.sort()
        res = []
        lo, hi = 0, len(nums)-1
        while lo<hi:
            sum = nums[lo] + nums[hi]
            cur_left = nums[lo]
            cur_right = nums[hi]
            if sum < target:
                while lo<hi and nums[lo] == cur_left:
                    lo += 1
            elif sum > target:
                while lo<hi and nums[hi] == cur_right:
                    hi -= 1
            else:
                res.append([lo, hi])
                while lo<hi and nums[lo] == cur_left:
                    lo += 1
                while lo<hi and nums[hi] == cur_right:
                    hi -= 1
        return res
    


# 3 sum
class Solution:
    def threeSum(self, nums, target):
        nums.sort()
        res = []
        i,n = 0, len(nums)
        while i < n:
            # 对 target - nums[i] 计算 twoSum
            tuples = self.twoSumTarget(nums, i + 1, target - nums[i])
            for tuple in tuples:
                tuple.append(nums[i])
                res.append(tuple)
            # 跳过第一个数字重复
            """
            注意两种写法：
            第一种写法：“往前看” 去重，总会先跳一步
            第二种写法：“往后看” 去重，如果不相同就需要手动跳一步
            """
            # # 方法1
            # while i< n and nums[i] == cur:
            #     i += 1
            # # i+= 1

            # 方法2
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res

    def threeSum(self, nums, target):
        nums.sort()
        res = []
        i = 0
        for i,num in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]:
                continue
            remain = target - num
            tuples = self.twoSumTarget(nums, i+1, remain)
            for tuple in tuples:
                res.append([num]+tuple)
        return res
    

# n sum
"""
一. base case的写法
    注意多个base case可以用 if if if, 也可以 if elif elif
    但是不需要else：因为每个base case都有return终结

二. 是否需要memo
    ❌ 会不会出现两个完全相同的 (ns,start,target)？
    不会。原因是：
    1. start 单调递增
        每一层递归都往右走：i+1。
        以 (start) 不会倒退，自然不会回到同一个起点。
    2. target 每次都被减去不同的 nums[i]
        所以即使 start 相同，target 也不会相同。
"""
class Solution:
    def fourSum(self, nums, target):
        return self.nSum(nums, 4, 0, target)

    def nSum(self, nums, n, start, target):
        nums.sort()
        res = []
        l = len(nums)
        # case 1 n个数超过list长度
        if n > l:
            return res
        # case 2 已经完成2sum
        if n == 1:
            return res
        
        if n == 2:
            return self.twoSum(nums, start, target)
        
        for i in range(start, l):
            if i > start and nums[i] == nums[i-1]:
                continue
            # 计算子问题
            remain = target - nums[i]
            tuples = self.nSum(nums, n-1, start+1, remain)
            for tuple in tuples:
                res.append(nums[i] + tuples)
        return res

    def twoSum(self, nums, start, target):
        res = []
        lo, hi = start, len(nums)-1
        while lo < hi:
            left, right = nums[lo], nums[hi]
            curSum=left+right

            if curSum < target:
                while lo<hi and nums[lo] == left:
                    lo +=  1
            elif curSum > target:
                while lo<hi and nums[hi] == right:
                    hi -= 1
            
            else:
                res.append([left, right])
                while lo<hi and nums[lo] == left:
                    lo +=  1
                while lo<hi and nums[hi] == right:
                    hi -= 1
        return res
