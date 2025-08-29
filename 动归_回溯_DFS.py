"""
⏰划重点

动归/DFS/回溯算法都可以看做二叉树问题的扩展，只是它们的关注点不同：

    动态规划算法属于分解问题（分治）的思路，它的关注点在整棵「子树」。
    回溯算法属于遍历的思路，它的关注点在节点间的「树枝」。
    DFS 算法属于遍历的思路，它的关注点在单个「节点」。
"""

"""
# 例子一：分解问题的思想体现
动态规划分解问题的思路，它的着眼点永远是结构相同的整个子问题，类比到二叉树上就是「子树」。
"""
def count(root):
    # 定义：输入一棵二叉树，返回这棵二叉树的节点总数
    if root is None:
        return 0
    # 当前节点关心的是两个子树的节点总数分别是多少
    # 因为用子问题的结果可以推导出原问题的结果
    leftCount = count(root.left)
    rightCount = count(root.right)
    # 后序位置，左右子树节点数加上自己就是整棵树的节点数
    return leftCount + rightCount + 1

"""
例子二：回溯算法的思想体现
🔍 一句话理解回溯算法
    回溯算法是“穷举所有可能解”的一种策略，适用于做选择 + 撤销选择的递归结构。

🌟 适用场景
你可以这样判断一个问题是否适合用回溯算法来解决：
    ✅ 你要找所有满足条件的结果（不是一个结果，而是所有）
    ✅ 问题具有**“选或不选”“试探路径”的结构**
    ✅ 常见问题：组合、排列、子集、N皇后、迷宫路径、括号生成、单词搜索等
        题目：给定 [1, 2, 3]，求它的全排列结果（即 [1,2,3], [1,3,2], …）

| 区别点     | DFS              | 回溯算法           |
| ------    | -----------      | -------------- |
| 目标       | 遍历结构（如所有节点| 找到所有方案（所有路径、解） |
| 状态记录    | 通常只关注当前节点  | 需要记录路径、做过哪些选择  |
| 撤销选择逻辑 | 不强调           | 每次递归后都要撤销试探的路径 |
| 是否记录解   | 通常不需要        | 每次到达合法叶子就记录一个解 |

回溯算法遍历的思路，它的着眼点永远是在节点之间移动的过程，类比到二叉树上就是「树枝」。

"""



"""
例子三：DFS 的思想体现
第三个例子，我给你一棵二叉树，请你写一个 traverse 函数，把这棵二叉树上的每个节点的值都加一
DFS 算法遍历的思路，它的着眼点永远是在单一的节点上，类比到二叉树上就是处理每个「节点」。
"""
def traverse(root):
    if root is None:
        return
    # 遍历过的每个节点的值加一
    root.val += 1
    traverse(root.left)
    traverse(root.right)



# DFS 算法把「做选择」「撤销选择」的逻辑放在 for 循环外面
"""
| 维度          | DFS              | 回溯               |
| --------     | ------------      | ---------------- |
| 着眼点        | 节点（Node）       | 路径/树枝（Branch）    |
| 用途          | 遍历整棵树/图       | 求解所有解（排列组合、N皇后等） |
| 「做选择」位置  | for 外（进入节点时）| for 内（尝试走路径前）    |
| 「撤销选择」位置 | for 外（退出节点时）| for 内（回退到上一步路径时） |

"""
def dfs(root):
    if root is None:
        return
    # 做选择
    print("enter node %s" % root)
    for child in root.children:
        dfs(child)
    # 撤销选择
    print("leave node %s" % root)

# 回溯算法把「做选择」「撤销选择」的逻辑放在 for 循环里面
# 关注的是“路径”的试探与撤销。
def backtrack(root):
    if root is None:
        return
    for child in root.children:
        # 做选择
        print("I'm on the branch from %s to %s" % (root, child))
        backtrack(child)
        # 撤销选择
        print("I'll leave the branch from %s to %s" % (child, root))



"""
后文 BFS 算法框架 就是从二叉树的层序遍历扩展出来的，常用于求无权图的最短路径问题。

"""
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = deque([root])
        # root 本身就是一层，depth 初始化为 1
        depth = 1

        while q:
            sz = len(q)
            # 遍历当前层的节点
            for _ in range(sz):
                cur = q.popleft()
                # 判断是否到达叶子结点
                if cur.left is None and cur.right is None:
                    return depth
                # 将下一层节点加入队列
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            # 这里增加步数
            depth += 1
        return depth