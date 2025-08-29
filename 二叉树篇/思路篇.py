"""
力扣第 226 题「翻转二叉树」
"""
# 「遍历」的思维模式解决
"""
前序：在递归处理左右子树之前处理当前节点
中序：在处理完左子树，即将进入右子树之前处理当前节点
后序：在左右子树都处理完后处理当前节点

❌ 为什么不能放在中序位置？
问题在于：
    你先访问了左子树
    然后交换了左右
    接着再访问右子树（此时的右子树，其实原来是左子树）
这就等于你把左子树遍历了两次，而原本的右子树没有遍历到，造成严重错误。
"""
class Solution:
    # 主函数
    def invertTree(self, root):
        # 遍历二叉树，交换每个节点的子节点
        self.traverse(root)
        return root

    # 二叉树遍历函数
    def traverse(self, root):
        if not root:
            return 
        
        # *** 前序位置 ***
        # 每一个节点需要做的事就是交换它的左右子节点
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # 遍历框架，去遍历左右子树的节点
        self.traverse(root.left)
        self.traverse(root.right)


# 「分解问题」的思维模式解决
"""
可以用 invertTree(x.left) 先把 x 的左子树翻转，再用 invertTree(x.right) 把 x 的右子树翻转，
最后把 x 的左右子树交换，这恰好完成了以 x 为根的整棵二叉树的翻转，即完成了 invertTree(x) 的定义。
"""

class Solution:
    # 定义：将以 root 为根的这棵二叉树翻转，返回翻转后的二叉树的根节点
    def invertTree(self, root):
        if root is None:
            return None
        # 利用函数定义，先翻转左右子树
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # 然后交换左右子节点
        root.left, root.right = right, left

        # 和定义逻辑自恰：以 root 为根的这棵二叉树已经被翻转，返回 root
        return root
    

"""
116. 填充每个节点的下一个右侧节点指针 | 力扣 | LeetCode |  🟠
"""

# ❌错误示例
# 孙子级的，爸爸1的右儿子， 爸爸2的左儿子连不上
def traverse(root):
    if root is None or root.left is None:
        return
    # 把左子节点的 next 指针指向右子节点
    root.left.next = root.right

    traverse(root.left)
    traverse(root.right)

"""
# 这样，一棵二叉树被抽象成了一棵三叉树，三叉树上的每个节点就是原先二叉树的两个相邻节点。
# 现在，我们只要实现一个 traverse 函数来遍历这棵三叉树，每个「三叉树节点」需要做的事就是把自己内部的两个二叉树节点穿起来：
"""
class Solution:
    # 主函数
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        # 遍历「三叉树」，连接相邻节点
        self.traverse(root.left, root.right)
        return root

    # 三叉树遍历框架
    def traverse(self, node1: 'Node', node2: 'Node') -> None:
        if not node1 or not node2:
            return
        # 前序位置 
        # 将传入的两个节点穿起来
        node1.next = node2 
        
        # 连接相同父节点的两个子节点
        self.traverse(node1.left, node1.right)
        self.traverse(node2.left, node2.right)
        # 连接跨越父节点的两个子节点
        self.traverse(node1.right, node2.left)



"""1、这题能不能用「遍历」的思维模式解决？

    乍一看感觉是可以的：对整棵树进行前序遍历，一边遍历一边构造出一条「链表」就行了：
    但是注意 flatten 函数的签名，返回类型为 void，也就是说题目希望我们在原地把二叉树拉平成链表。
    这样一来，没办法通过简单的二叉树遍历来解决这道题了。"""
# 🔥 还是值得注意一下这种写法
# 虚拟头节点，dummy.right 就是结果
dummy = TreeNode(-1)
# 用来构建链表的指针
p = dummy

def traverse(root: TreeNode):
    if root is None:
        return
    # 前序位置
    p.right = TreeNode(root.val)
    p = p.right

    traverse(root.left)
    traverse(root.right)

"""
正确思路
🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
和子树有关，在后序位置写代码了。
🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
1、先利用 flatten(x.left) 和 flatten(x.right) 将 x 的左右子树拉平。

2、将 x 的右子树接到左子树下方，然后将整个左子树作为右子树。
    1
   / \
  2   5
 / \   \
3   4   6

    1
   / \
  2   5
   \   \
    3   6
     \
      4


1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

"""
class Solution:
    # 定义：将以 root 为根的树拉平为链表
    def flatten(self, root) -> None:
        # base case
        if root is None:
            return

        # 利用定义，把左右子树拉平
        self.flatten(root.left)
        self.flatten(root.right)
        """
        注意选后序位置，自下而上的迭代
        """
        # 后序遍历位置
        # 1、左右子树已经被拉平成一条链表
        left = root.left
        right = root.right

        # 2、将左子树作为右子树
        root.left = None
        root.right = left

        # 3、将原先的右子树接到当前右子树的末端
        p = root
        while p.right is not None:
            p = p.right
        p.right = right 