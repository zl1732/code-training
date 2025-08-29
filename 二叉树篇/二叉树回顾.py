"""
🔥🔥🔥🔥🔥🔥
前序位置是进入一个节点的时候，后序位置是离开一个节点的时候
🔥🔥🔥🔥🔥🔥
"""


"""
单链表和数组的遍历可以是迭代的，也可以是递归的
    所谓前序位置，就是刚进入一个节点（元素）的时候，
    后序位置就是即将离开一个节点（元素）的时候，
    那么进一步，你把代码写在不同位置，代码执行的时机也不同：


前序位置 vs 后序位置

    前序：→ → → →
    节点：[1]→[2]→[3]→[4]→[5]
    后序：<== <== <== <==
          ↑                 ↑
       前序处理         后序处理
                     base case 到达终点

说明：
    前序：1 2 3 4 5
    后序：5 4 3 2 1
    - 用于理解递归结构中的“前序/后序”操作时机。
"""

# 迭代遍历数组
def traverse(arr: List[int]) -> None:
    for i in range(len(arr)):
        pass

# 递归遍历数组
def traverse_recursive(arr: List[int], i: int) -> None:
    if i == len(arr):
        return
    # 前序位置
    traverse_recursive(arr, i + 1)
    # 后序位置


# 迭代遍历单链表
def traverse_linked_list(head: ListNode) -> None:
    p = head
    while p:
        p = p.next

# 递归遍历单链表
def traverse_linked_list_recursive(head: ListNode) -> None:
    if not head:
        return
    # 前序位置 正序
    traverse_linked_list_recursive(head.next)
    # 后序位置 倒序


"""
遍历 vs 分解
    1、是否可以通过遍历一遍二叉树得到答案？
    如果可以，用一个 traverse 函数配合外部变量来实现，
    这叫「遍历」的思维模式。

    2、是否可以定义一个递归函数，通过子问题（子树）的答案推导出原问题的答案？
    如果可以，写出这个递归函数的定义，并充分利用这个函数的返回值，
    这叫「分解问题」的思维模式。
"""

"""
建议你也遵循我的这种风格：
    1. 遍历思路解题时函数签名一般是 void traverse(...)，
        * 没有返回值，靠更新外部变量来计算结果

    2. 分解问题思路解题时函数名根据该函数具体功能而定
        * 而且一般会有返回值，返回值是子问题的计算结果。

        3. 拓展
            回溯算法核心框架 中给出的函数签名一般也是没有返回值的 void backtrack(...)
            而在 动态规划核心框架 中给出的函数签名是带有返回值的 dp 函数。
            这也说明它俩和二叉树之间千丝万缕的联系。
"""

"""
例题：
    力扣第 104 题「二叉树的最大深度」最大深度，最大深度就是根节点到「最远」叶子节点的最长路径上的节点数
"""
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
        """
        对 res 的更新，放到前中后序位置都可以，
        只要保证在进入节点之后，离开节点之前
        （即 depth 自增之后，自减之前）就行了。
        """
        if root.left is None and root.right is None:
            self.res = max(self.res, self.depth)
        self.traverse(root.left)
        self.traverse(root.right)

        # 后序遍历位置（离开节点）减少深度
        self.depth -= 1


# 分解问题的思路
"""
分解问题计算答案的思路：
1. 主要的代码逻辑集中在后序位置
    通过子树的最大深度推导出原树的深度
    首先需要算出左右子树的最大深度，最后推出原树的最大深度

"""
class Solution:
    # 定义：输入一个节点，返回以该节点为根的二叉树的最大深度
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # 利用定义，计算左右子树的最大深度
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)

        # 根据左右子树的最大深度推出原二叉树的最大深度
        # 整棵树的最大深度等于左右子树的最大深度取最大值，
        # 然后再加上根节点自己
        return 1 + max(leftMax, rightMax)
    

#第 144 题「二叉树的前序遍历」
# 用分解的思路
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        # # 没必要写：避免对叶子节点的左右孩子（即 None）继续递归调用，
        # # 减少了一点递归调用的开销，逻辑上也是完全正确的。
        # if root.left is None and root.right is None:
        #     return [root.val]
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        # return是后序位置，但是return里的加法保持前序！
        return [root.val] + left + right

# labuladong 写法
class Solution:
    def preorderTraversal(self, root):
        res = []
        if root == None:
            return res
        # 前序 在第一个
        res.append(root.val)
        res.extend(self.preorderTraversal(root.left))
        # 中序 res.append(root.val)
        res.extend(self.preorderTraversal(root.right)) 
        # 后序 res.append(root.val)
        return res

"""
虽然是“在后序位置写的 return”，但：
你拼接结果时把 root.val 放在最前面（return [root.val] + left + right）
左右子树的遍历结果按顺序拼接，整体构造的就是前序遍历结果

想象你在写作文：
    最终把整篇文章打印出来的行为是“后序”动作（最后一个动作） (return在最后)
    但你在打印之前，就已经把段落安排成了“开头 + 主体 + 结尾”这个顺序 ([root.val] + left + right)
    所以打印虽然是“后”，但文章结构仍然是“前 → 中 → 后”

总结：
    前序：return root.val + 左 + 右
    中序：return 左 + root.val + 右
    后序：return 左 + 右 + root.val
"""

"""
💥💥💥💥 注意
这种写法简洁漂亮，但存在一个潜在性能问题：频繁地做列表拼接操作（+）可能导致 O(N^2) 的复杂度。
✅ Java(python) 中的问题：addAll 是 O(N)
res.add(root.val);
res.addAll(left);  O(N)
res.addAll(right); O(N)

ArrayList.addAll(...) 的复杂度是 O(M)，因为它要逐个复制元素
最坏情况：二叉树退化成链表，导致 N + (N-1) + (N-2) + ... + 1 = O(N^2) 的开销

为什么？
    ✅  每次 + 就是“全量复制”
    假设：
        当前节点是第 k 层的节点（从根节点开始算）
        那它的左子树还有 N - k 个节点（退化成链表时）
        left 的长度是 N - k
        right 是 []
    你执行这句拼接：
        return [root.val] + left
    发生了什么？
        [root.val] 是一个长度为 1 的新列表
        left 是一个列表，长度是 N - k
        Python 会创建一个 新的列表，长度为 1 + (N - k)
        然后把这两个列表中的元素 一个一个复制进去
    所以复制的元素个数是：
        1 + (N - k) = N - k + 1
    复制动作是 每个元素单独拷贝到新列表，总时间是 O(N - k + 1)

    
😌😌😌😌 遍历方法是 append 是 O(1) 总体是 O(N)
"""


"""
🔥🔥🔥🔥 一旦你发现题目和子树有关，那大概率要给函数设置定义和返回值，在后序位置写代码。

前中后序位置的代码，能力依次增强。
    前序位置: 父节点信息
    中序位置：父 + 左
    后序位置：父 + 左 + 右
所以，某些情况下把代码移到后序位置效率最高；有些事情，只有后序位置的代码能做。

中序位置主要用在 BST 场景中，你完全可以把 BST 的中序遍历认为是遍历有序数组。

后序位置：每个节点的左右子树各有多少节点
    一般都使用「分解问题」的思路。
    因为当前节点接收并利用了子树返回的信息，
    这就意味着你把原问题分解成了当前节点 + 左右子树的子问题。
"""

# 前序计算子树深度
# traverse 遍历每个节点的时候还会调用递归函数 maxDepth，而 maxDepth 是要遍历子树的所有节点的，所以最坏时间复杂度是 O(N^2)。
class Solution:

    def __init__(self):
        # 记录最大直径的长度
        self.maxDiameter = 0

    def diameterOfBinaryTree(self, root):
        # 对每个节点计算直径，求最大直径
        self.traverse(root)
        return self.maxDiameter

    # 遍历二叉树
    def traverse(self, root):
        if root is None:
            return
        # 对每个节点计算直径
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        myDiameter = leftMax + rightMax
        # 更新全局最大直径
        self.maxDiameter = max(self.maxDiameter, myDiameter)
        
        self.traverse(root.left)
        self.traverse(root.right)

    # 计算二叉树的最大深度
    def maxDepth(self, root):
        if root is None:
            return 0
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        return 1 + max(leftMax, rightMax)

# 后序位置计算
class Solution:
    def __init__(self):
        # 记录最大直径的长度
        self.maxDiameter = 0

    def diameterOfBinaryTree(self, root):
        self.maxDepth(root)
        return self.maxDiameter

    def maxDepth(self, root):
        if root is None:
            return 0
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        # 后序位置，顺便计算最大直径
        myDiameter = leftMax + rightMax
        self.maxDiameter = max(self.maxDiameter, myDiameter)

        return 1 + max(leftMax, rightMax)


"""
注意：
“结构性问题（如求深度）” vs “过程性问题（如遍历）”的关键区别：

✅ 一类 return 是“结构控制”型 —— 有顺序意义
    # 前序遍历
    return [root.val] + left + right
    # 中序遍历
    return left + [root.val] + right
    # 后序遍历
    return left + right + [root.val]

✅ 另一类 return 是“数值合并”型 —— 无顺序意义
    return 的本质是“合并左右子问题的值”
    它只是 结果的传递、组合，不代表访问顺序
    例：
    return 1 + max(left, right)       # 求深度
    return is_bst_left and is_bst_right and valid(root)  # 判断 BST
    return max(left + right, ...)     # 求路径和等

🔥🔥🔥   “以节点为单位做动作”的（遍历型）
            vs
        “以子树为单位组合结果”的（结构型）
"""

