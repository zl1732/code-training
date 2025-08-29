"""
回溯算法和我们常说的 DFS 算法基本可以认为是同一种算法

站在回溯树的一个节点上，你只需要思考 3 个问题：

    1、路径：也就是已经做出的选择。

    2、选择列表：也就是你当前可以做的选择。

    3、结束条件：也就是到达决策树底层，无法再做选择的条件。

🔥🔥🔥 算法框架 🔥🔥🔥
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
"""

# 排列组合
from typing import List

class Solution:
    def __init__(self):
        self.res = []

    # 主函数，输入一组不重复的数字，返回它们的全排列
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 记录「路径」
        track = []
        # 「路径」中的元素会被标记为 true，避免重复使用
        used = [False] * len(nums)
        
        self.backtrack(nums, track, used)
        return self.res

    # 路径：记录在 track 中
    # 选择列表：nums 中不存在于 track 的那些元素（used[i] 为 false）
    # 结束条件：nums 中的元素全都在 track 中出现
    def backtrack(self, nums: List[int], track: List[int], used: List[bool]):
        # 触发结束条件
        if len(track) == len(nums):
            self.res.append(track.copy())
            return
        
        for i in range(len(nums)):
            # 排除不合法的选择
            if used[i]: 
                # nums[i] 已经在 track 中，跳过
                continue
            # 做选择
            track.append(nums[i])
            used[i] = True
            # 进入下一层决策树
            self.backtrack(nums, track, used)
            # 取消选择
            track.pop()
            used[i] = False

"""
关于：  
        主函数call的self.backtrack(nums, track, used)，
        这里nums是[1,2,3]，怎么可能退回到[False，False，False] 
这个问题：

    track.append(nums[i])
    used[i] = True

    self.backtrack(nums, track, used)

    track.pop()
    used[i] = False  # <= 就是这一行！主动撤销“副作用”

虽然 used 是引用传递进去的，但我们在 每一层递归返回时，都会把 used[i] 手动设置回 False。
这样就相当于“恢复了现场”，像时间倒流一样，变量回到了递归前的状态。

def f(u):
    u[0] = True
    print("在函数里：", u)
    u[0] = False  # 恢复！
    print("恢复后：", u)

used = [False, False]
f(used)
print("函数外：", used)

在函数里： [True, False]
恢复后： [False, False]
函数外： [False, False]

"""