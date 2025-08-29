
"""
| 思路   | 特点                 | 举例                    |
| ---- | ------------------ | --------------------- |
| 回溯法  | **枚举所有可能路径**，遍历多叉树 | 子集、排列组合、全排列等          |
| 分解问题 | **把大问题分成小问题来解决**   | 斐波那契数列、背包问题、子集和、最短路径等 |

"""
class Solution:
    def __init__(self):
        self.res = []

    # 主函数，输入一组不重复的数字，返回它们的全排列
    def permute(self, nums):
        # 记录「路径」
        track = []
        # 「路径」中的元素会被标记为 true，避免重复使用
        used = [False] * len(nums)
        
        self.backtrack(nums, track, used)
        return self.res

    # 路径：记录在 track 中
    # 选择列表：nums 中不存在于 track 的那些元素（used[i] 为 false）
    # 结束条件：nums 中的元素全都在 track 中出现
    def backtrack(self, nums, track, used):
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
初始状态：track = [], used = [F, F]

第 1 层：
  i=0 → 选择 1 → track = [1], used = [T, F]

    第 2 层：
      i=0 → 跳过（1 已用）
      i=1 → 选择 2 → track = [1,2], used = [T,T]
        满足终止条件，res += [[1,2]]

    回退：track = [1], used = [T,F]
    再回退：track = [], used = [F,F]

  i=1 → 选择 2 → track = [2], used = [F,T]

    第 2 层：
      i=0 → 选择 1 → track = [2,1], used = [T,T]
        满足终止条件，res += [[2,1]]

最终结果：[[1,2], [2,1]]

"""


"""
其实很简单，编写递归算法只可能有两种思维模式，都尝试套用一下，必然有一种能写出来：
一种是「遍历」的思维模式，另一种是「分解问题」的思维模式。

💡💡💡划重点
如果你想用「分解问题」的思维模式来写递归算法，那么这个递归函数一定要有一个清晰的定义，说明这个函数参数的含义是什么，返回什么结果。
"""

# 104. 二叉树的最大深度 | 力扣 | LeetCode |  🟢
# 分解问题的思路
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)

        # 根据左右子树的最大深度推出原二叉树的最大深度
        # 整棵树的最大深度等于左右子树的最大深度取最大值，
        # 然后再加上根节点自己
        return 1 + max(leftMax, rightMax)

# 遍历的思维模式
# 遍历的思路
class Solution:

    def __init__(self):
        # 记录遍历到的节点的深度
        self.depth = 0
        # 记录最大深度
        self.res = 0

    def maxDepth(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.res

    # 遍历二叉树
    def traverse(self, root: TreeNode):
        if root is None:
            return

        # 前序遍历位置（进入节点）增加深度
        self.depth += 1
        # 遍历到叶子节点时记录最大深度
        if root.left is None and root.right is None:
            self.res = max(self.res, self.depth)
        self.traverse(root.left)
        self.traverse(root.right)

        # 后序遍历位置（离开节点）减少深度
        self.depth -= 1