"""
形式一、元素无重不可复选，即 nums 中的元素都是唯一的，每个元素最多只能被使用一次，这也是最基本的形式。
以组合为例，如果输入 nums = [2,3,6,7]，和为 7 的组合应该只有 [7]。

形式二、元素可重不可复选，即 nums 中的元素可以存在重复，每个元素最多只能被使用一次。
以组合为例，如果输入 nums = [2,5,2,1,2]，和为 7 的组合应该有两种 [2,2,2,1] 和 [5,2]。

形式三、元素无重可复选，即 nums 中的元素都是唯一的，每个元素可以被使用若干次。
以组合为例，如果输入 nums = [2,3,6,7]，和为 7 的组合应该有两种 [2,2,3] 和 [7]。
"""

"""
上面用组合问题举的例子，但排列、组合、子集问题都可以有这三种基本形式，所以共有 9 种变化。
除此之外，题目也可以再添加各种限制条件，比如让你求和为 target 且元素个数为 k 的组合，那这么一来又可以衍生出一堆变体
"""


# 此页内容
# 1 子集（元素无重不可复选）
# 2 组合（元素无重不可复选）
# 3 排列（元素无重不可复选）

# 4 子集/组合（元素可重不可复选）
# 5 排列（元素可重不可复选）

# 6 子集/组合（元素无重可复选）
# 7 排列（元素无重可复选）



# 第一种
# 子集（元素无重不可复选）
"""
子集（元素无重不可复选）
力扣第 78 题「子集」就是这个问题：
题目给你输入一个无重复元素的数组 nums，其中每个元素最多使用一次，请你返回 nums 的所有子集。

比如输入 nums = [1,2,3]，算法应该返回如下子集：
[ [],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3] ]
"""


"""
第一张图:

    S_0
      []
     / | \
    1  2  3
  [1] [2] [3]


------------------------------------------------------

第二张图:

    S_1
       [1]    [2]    [3]
      /   \     \
     2     3     3
  [1,2] [1,3] [2,3]

------------------------------------------------------

完整回溯树（子集生成）:

               []
        /       |       \
     [1]       [2]      [3]
    /   \        \
 [1,2] [1,3]    [2,3]
   |
[1,2,3]


为什么集合 [2] 只需要添加 3，而不添加前面的 1 呢？
因为集合中的元素不用考虑顺序，[1,2,3] 中 2 后面只有 3，如果你添加了前面的 1，那么 [2,1] 会和之前已经生成的子集 [1,2] 重复。
🔥🔥 我们通过保证元素之间的相对顺序不变来防止出现重复的子集


🔥🔥 第 n 层的所有节点就是大小为 n 的所有子集。
    * 大小为2的子集，在第二层

算法核心：
- 回溯 + 递归：

"""
from typing import List
class Solution:
    def __init__(self):
        self.res = []
        self.track = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums: List[int], start: int) -> None:
        # 前序位置，每个节点的值都是一个子集
        self.res.append(list(self.track))
        for i in range(start, len(nums)):
            self.track.append(nums[i])
            # 通过 start 参数控制树枝的遍历，避免产生重复的子集
            self.backtrack(nums, i + 1)
            self.track.pop()



# 第二种
# 组合（元素无重不可复选）
"""
组合（元素无重不可复选）
组合和子集是一样的：大小为 k 的组合就是大小为 k 的子集。
给你输入一个数组 nums = [1,2..,n] 和一个正整数 k，请你生成所有大小为 k 的子集。


               []
        /       |       \
     [1]       [2]      [3]
    /   \        \
  -------------------— 
 |[1,2] [1,3]    [2,3]|  # k=2的子集
  -------------------—
   |
[1,2,3]
"""

class Solution:
    def __init__(self):
        self.res = []
        self.track = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(1, n, k)
        return self.res

    def backtrack(self, start: int, n: int, k: int) -> None:
        # base case
        if k == len(self.track):
            # 遍历到了第 k 层，收集当前节点的值
            self.res.append(self.track.copy())
            return
        
        for i in range(start, n+1):
            self.track.append(i)
            self.backtrack(i + 1, n, k)
            self.track.pop()



# 第三种
# 排列（元素无重不可复选）
"""
排列（元素无重不可复选）

力扣第 46 题「全排列」就是标准的排列问题：
给定一个不含重复数字的数组 nums，返回其所有可能的全排列。

nums = [1,2,3]
[
    [1,2,3],[1,3,2],
    [2,1,3],[2,3,1],
    [3,1,2],[3,2,1]
]

全排列回溯树（以 [1, 2, 3] 为例）:

                    []
          /          |          \
        [1]          [2]         [3]
       /   \        /   \       /   \
    [1,2]  [1,3]  [2,1] [2,3] [3,1] [3,2]
      |      |      |     |      |     |
[1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]

"""

"""
✅ 为什么要用 used 数组？
    在全排列问题中每个元素只能使用一次；
    同一层不能重复选择已经选过的元素。
    !!!!! 只用一个used数组控制就够了，不需要start

如果没有 used，回溯过程中无法判断一个元素是否已经在当前路径中，可能会出现重复选择的问题。
例如 nums = [1,2,3]，如果不加限制，你可能得到 [1,1,2] 这样的错误结果。
"""

class Solution:
    """
    在这里声明比较好，避免下次调用时被污染
    """
    def permute(self, nums: List[int]):
        self.res = []
        self.track = []
        # track 中的元素会被标记为 true
        self.used = [False] * len(nums)
        self.backtrack(nums)
        return self.res
    
    def backtrack(self, nums: List[int]) -> None:
        # base case，到达叶子节点
        if len(self.track) == len(nums): #（k层：K）
            self.res.append(self.track[:])
            return
        
        # 回溯算法标准框架
        for i in range(len(nums)):
            # 已经存在 track 中的元素，不能重复选择
            if self.used[i]:
                continue

            self.used[i] = True
            self.track.append(nums[i])
            self.backtrack(nums)
            self.track.pop()
            self.used[i] = False




# 延伸
# 元素个数为 k 的排列
def backtrack(nums: List[int], k: int) -> None:
    # base case，到达第 k 层，收集节点的值
    if len(track) == k:
        res.append(track[:])
        return


# 第四种：
# 子集/组合（元素可重不可复选）
"""
力扣第 90 题「子集 II
nums = [1,2,2]，你应该输出：
[ [],[1],[2],[1,2],[2,2],[1,2,2] ]


                [ ]
            /    |    \
         1 /     |2    \ 2'
          /      |      \
        [1]     [2]      [2']
       /  \      |
     2/    \2'  [2,2']
     /      \
   [1,2]   [1,2']
     |
  [1,2,2']

得到：
[ 
    [],
    [1],[2],[2'],
    [1,2],[1,2'],[2,2'],
    [1,2,2']
]

[2] 和 [1,2] 这两个结果出现了重复，所以我们需要进行剪枝，如果一个节点有多条值相同的树枝相邻，则只遍历第一条，剩下的都剪掉

                [ ]            start = 1
            /    |   \
         1 /     |2    ❌ 2'   i =  1 2 3
          /      |      \
        [ ]     [2]      *[2'] start = 2
       /  \      |
     2/    ❌2'  [2,2']        i = 1, 2; 1
     /      \
   [1,2]   *[1,2]
     |
   2'|
     |
  [1,2,2']

代码：先对序列进行排序，让相同的元素靠在一起，如果发现 nums[i] == nums[i-1]，则跳过：

start -- 层数
i     -- 数列中index
"""

class Solution:
    def __init__(self):
        self.res = []
        self.track = []
    
    def subsetsWithDup(self, nums: List[int]):
        # 先排序，让相同的元素靠在一起
        nums.sort()
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums: List[int], start: int) -> None:
        # 前序位置，每个节点的值都是一个子集
        self.res.append(self.track[:])
        
        for i in range(start, len(nums)):
            # 剪枝逻辑，值相同的相邻树枝，只遍历第一条
            if i > start and nums[i] == nums[i - 1]: # i>start [1,2,2‘] start在1，i在2’
                continue
            self.track.append(nums[i])
            print(self.track)
            self.backtrack(nums, i + 1)
            self.track.pop()


Solution().subsetsWithDup([1,2,2])
"""
✅ 遍历路径演示
print("start:",start+1, "i:",i+1)
start: 1 i: 1
[1]
start: 2 i: 2
[1, 2]
start: 3 i: 3
[1, 2, 4]
start: 2 i: 3
[1, 4]
start: 1 i: 2
[2]
start: 3 i: 3
[2, 4]
start: 1 i: 3
[4]
start: 1 第1排， i:1 第1个数    start -- 层数
start: 3 第3排， i:3 第3个数    i     -- 数列中index


✅ 为什么要这个条件？
假设没有 i > start，只写 if nums[i] == nums[i-1]: continue：

    那么在递归深入时（比如从 [1,2] 到 [1,2,2']），也会触发这个判断。
    但 [1,2,2'] 是一个合法的子集，不应该被跳过！

    
# 如果没有if i > start
start: 1 i: 1
[1]
start: 2 i: 2
[1, 2]
start: 3 i: 3
start: 2 i: 3
start: 1 i: 2
[2]
start: 3 i: 3
start: 1 i: 3
"""

# 衍生
# 给你输入 candidates 和一个目标和 target，从 candidates 中找出中所有和为 target 的组合。
"""
力扣第 40 题「组合总和 II」：
思路：额外用一个 trackSum 变量记录回溯路径上的元素和，然后将 base case 改一改
"""

class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.trackSum = 0
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return self.res
        candidates.sort()
        self.backtrack(candidates, 0, target)
        return self.res
    
    # 回溯算法主函数
    def backtrack(self, nums: List[int], start: int, target: int):
        # base case，达到目标和，找到符合条件的组合
        if self.trackSum == target:
            self.res.append(self.track[:])
            return
        # base case，超过目标和，直接结束
        if self.trackSum > target:
            return
        
        for i in range(start, len(nums)):
            # 剪枝逻辑，值相同的树枝，只遍历第一条
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.track.append(nums[i])
            self.trackSum += nums[i]
            # 递归遍历下一层回溯树
            self.backtrack(nums, i + 1, target)
            self.track.pop()
            self.trackSum -= nums[i]



# 第五种
# 排列（元素可重不可复选）
"""
力扣第 47 题「全排列 II」

[1,1,2]
start []
 ├─ 1(第0个) → [1]
 │    ├─ 1(第1个, 不能选，因为used[0]=False时会被剪枝)
 │    └─ 2 → [1,2]
 │         └─ 1 → [1,2,1]
 └─ 1(第1个, 跳过，因为前一个相同元素没用过)
 └─ 2 → [2]
      └─ 1(第0个) → [2,1]
           └─ 1(第1个) → [2,1,1]
    
nums = [1,1,2]
第一步：选第一个 1（i=0）
track = [1(first)]
used = [True, False, False]
然后递归，继续生成 [1,1,2]、[1,2,1] 这些结果。
当这条分支所有排列都生成完毕后，会回溯：
撤销 i=0 的选择
track = []
used = [False, False, False]

第二步：走到第二个 1（i=1）
这时候确实是你说的：
used = [False, False, False]
想选 i=1 → 第二个 1。
→ 所以这时候会 continue，跳过第二个 1。
"""

class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.used = []
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 先排序，让相同的元素靠在一起
        nums.sort()
        self.used = [False] * len(nums)
        self.backtrack(nums)
        return self.res
    
    def backtrack(self, nums: List[int]) -> None:
        if len(self.track) == len(nums):
            self.res.append(self.track[:])
            return

        for i in range(len(nums)):
            if self.used[i]:
                continue
            # 新添加的剪枝逻辑，固定相同的元素在排列中的相对位置
            if i > 0 and nums[i] == nums[i - 1] and not self.used[i - 1]:
                continue
            self.track.append(nums[i])
            self.used[i] = True
            self.backtrack(nums)
            self.track.pop()
            self.used[i] = False






# 第六种
# 子集/组合（元素无重可复选）
"""
力扣第 39 题「组合总和」
candidates = [1,2,3], target = 3，算法应该返回：
[ [1,1,1],[1,2],[3] ]

这道题实际上也是子集问题：candidates 的哪些子集的和为 target？
如果我想让每个元素被重复使用，我只要把 i + 1 改成 i 即可：
"""
def backtrack(nums: List[int], start: int):
    for i in range(start, len(nums)):
        # ...
        backtrack(nums, i)  #这里不是i+1了，因为可以复用 
        # ...

"""
当然，这样这棵回溯树会永远生长下去，所以我们的递归函数需要设置合适的 base case 以结束算法
即路径和大于 target 时就没必要再遍历下去了。
"""

class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.trackSum = 0

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return self.res
        self.backtrack(candidates, 0, target)
        return self.res

    # 回溯算法主函数
    def backtrack(self, nums: List[int], start: int, target: int) -> None:
        # base case，找到目标和，记录结果
        if self.trackSum == target:
            self.res.append(list(self.track))
            return
        # base case，超过目标和，停止向下遍历
        if self.trackSum > target:
            return

        for i in range(start, len(nums)):
            self.trackSum += nums[i]
            self.track.append(nums[i])
            # 同一元素可重复使用，注意参数
            self.backtrack(nums, i, target)
            self.trackSum -= nums[i]
            self.track.pop()


# 第七种
# 排列（元素无重可复选）
"""
nums = [1,2,3]，那么这种条件下的全排列共有 3^3 = 27 种：
[
  [1,1,1],[1,1,2],[1,1,3],[1,2,1],[1,2,2],[1,2,3],[1,3,1],[1,3,2],[1,3,3],
  [2,1,1],[2,1,2],[2,1,3],[2,2,1],[2,2,2],[2,2,3],[2,3,1],[2,3,2],[2,3,3],
  [3,1,1],[3,1,2],[3,1,3],[3,2,1],[3,2,2],[3,2,3],[3,3,1],[3,3,2],[3,3,3]
]
"""
class Solution:
    
    def __init__(self):
        self.res = []
        self.track = []
    
    def permuteRepeat(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums)
        return self.res

    def backtrack(self, nums: List[int]) -> None:
        if len(self.track) == len(nums):
            self.res.append(self.track[:])
            return

        # 回溯算法标准框架
        for i in range(len(nums)):
            self.track.append(nums[i])
            self.backtrack(nums)
            self.track.pop()



###### 总结：######

# 组合: start控制起始点 + self.backtrack(nums, i + 1)
# 排列: self.used
        # for i in range(len(nums)):
        #     self.backtrack(nums)
# 有重复不可复选: if i > start and nums[i] == nums[i-1]
# 需要提前终止：if ==: append+return; if >: return

#（衍生）
# 全排列: 遵循基本回溯框架
        # for i in range(len(nums)):
        #     self.backtrack(nums)
# 可重组合: 下一层递归不用i+1
        # for i in range(start, len(nums)):
        #     self.backtrack(nums, i)
# 可重排列: if i > 0 and nums[i] == nums[i - 1] and not self.used[i - 1]:




"""
#形式一、元素无重不可复选，即 nums 中的元素都是唯一的，每个元素最多只能被使用一次
"""
# 组合/子集问题回溯算法框架
def backtrack(nums: List[int], start: int):
    for i in range(start, len(nums)):
        track.append(nums[i])
        backtrack(nums, i + 1)
        track.pop()

# 排列问题回溯算法框架
def backtrack(nums: List[int]):
    for i in range(len(nums)):
        if used[i]:
            continue

        used[i] = True
        track.append(nums[i])
        backtrack(nums)
        track.pop()
        used[i] = False
        

"""
形式二、元素可重不可复选，即 nums 中的元素可以存在重复，每个元素最多只能被使用一次
"""
nums = None

nums.sort()
# 组合/子集问题回溯算法框架
def backtrack(nums: List[int], start: int):
    for i in range(start, len(nums)):
        # 剪枝逻辑，跳过值相同的相邻树枝
        if i > start and nums[i] == nums[i - 1]:
            continue
        track.append(nums[i])
        backtrack(nums, i + 1)
        track.pop()


nums.sort()
# 排列问题回溯算法框架
def backtrack(nums: List[int]):
    for i in range(len(nums)):
        if used[i]:
            continue
        # 剪枝逻辑，固定相同的元素在排列中的相对位置
        if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
            continue

        used[i] = True
        track.append(nums[i])
        backtrack(nums)
        track.pop()
        used[i] = False


"""
形式三、元素无重可复选，即 nums 中的元素都是唯一的，每个元素可以被使用若干次
"""
# 组合/子集问题回溯算法框架
def backtrack(nums: List[int], start: int):
    for i in range(start, len(nums)):
        track.append(nums[i])
        backtrack(nums, i)
        track.pop()


# 排列问题回溯算法框架
def backtrack(nums: List[int]):
    for i in range(len(nums)):
        track.append(nums[i])
        backtrack(nums)
        track.pop()