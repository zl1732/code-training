#寻找一个元素

"""
1. 第一个效率高
    如果在左子树找到目标节点，没有必要去右子树找了
    找到立刻返回，效率高
"""
# 方法1 前序立刻return
def find(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return None
    
    if root.val == val:
        return root
    
    left = find(root.left, val)
    if left:
        return left
    
    right = find(root.right, val)
    if right:
        return right
    # 实在找不到了
    return None

"""
2. 第二个效率低
    这段代码还是会去右子树找一圈，所以效率相对差一些。
"""
# 方法2 前序最后return
def find(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return None
    
    if root.val == val:
        return root
    
    left = find(root.left, val)
    right = find(root.right, val)
    # 看看哪边找到了
    return left if left else right

"""
3. 效率更低
    要找的目标节点恰好就是根节点, 这种写法必然会遍历二叉树的每一个节点。
"""
# 方法3 后序
def find(root: TreeNode, val: int) -> TreeNode:
    if root is None:
        return None
    
    left = find(root.left, val)
    right = find(root.right, val)
    # 后序位置，看看 root 是不是目标节点
    if root.val == val:
        return root
    # root 不是目标节点，再去看看哪边的子树找到了
    return left if left else right



# 最近公共祖先问题
"""
root 里找 p, q 的公共祖先LCA

如果一个节点能在 左右子树中 分别找到 p 和 q 则该节点为 LCA 节点。
"""
# 基础框架 定义：在以 root 为根的二叉树中寻找值为 val1 或 val2 的节点
def find(root, val1, val2):
    if root is None:
        return None
    if root.val == val1 or root.val == val2:
        return root
    
    left = find(root.left, val1, val2)
    right = find(root.right, val1, val2)

    return left if left is not None else right


# 框架
# 在二叉树中寻找 val1 和 val2 的最近公共祖先节点
def find(self, root: 'TreeNode', val1: int, val2: int) -> 'TreeNode':
    if root is None:
        return None
    if root.val == val1 or root.val == val2:
        return root
    
    left = self.find(root.left, val1, val2)
    right = self.find(root.right, val1, val2)

    # 在此处新增: 后序位置判断LCA节点
    if left is not None and right is not None:
        return root
    
    return left if left is not None else right


# 如果你非要优化，只能用一个外部变量来辅助判断是否已经找到答案，如果已经找到 LCA，则不再继续遍历二叉树：
class Solution:
    def __init__(self):
        # 用一个外部变量来记录是否已经找到 LCA 节点
        self.lca = None

    def find(self, root: 'TreeNode', val1: int, val2: int) -> 'TreeNode':
        if root is None:
            return None
        # 如果已经找到 LCA 节点，直接返回
        if self.lca is not None:
            return None

        if root.val == val1 or root.val == val2:
            return root
        left = self.find(root.left, val1, val2)
        right = self.find(root.right, val1, val2)
        if left is not None and right is not None:
            # 当前节点是 LCA 节点，记录下来
            self.lca = root 
            return root
        
        return left if left is not None else right
    







# 236题 p q 确定存在
"""
只是告诉“当前这个子树里我已经找到了一个目标节点”，把这个信息一路往上“冒泡”。
最后的答案是在后序位置（拿到了 left、right 之后）决策出来的：
    左右都非空 → 当前 root 就是最近公共祖先
    否则把非空的那个 left/right 往上抛
"""
def lowestCommonAncestor(root, p, q):
    if not root:
        return None
    if root == p or root == q:        # ← 这里就是你说的“前序位置”return
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    return left or right



# 1644题 p q 不一定存在
"""
真正不能做的，是：一旦在某个地方遇到 p 或 q，就直接认定它是答案，整棵树的 DFS 提前结束。
对于 1644，这样会导致：
👉 只要树里有 p，不管 q 在不在树里，你最后都会返回个非空节点，而题目要求这种情况返回 None。
"""
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        self.foundP = False
        self.foundQ = False
        lca = self.dfs(root, p, q)
        if self.foundP and self.foundQ:
            return lca
        return None

    def dfs(self, root, p, q):
        if not root:
            return None
        
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)

        # 也可以在前序位置改两个flag，但是return必须在后序位置
        # 如果在前序return，也就是在两个递归前面，递归就执行不了，没法继续往下走
        # 写在后序其实是已经递归完毕往上（往回）走的时候了
        if root == p:
            self.foundP = True
            return root
        if root == q:
            self.foundQ = True
            return root
        
        if left and right:
            return root
        return left or right



### LCA 在 BST 中
"""
假设 val1 < val2，那么 val1 <= root.val <= val2 则说明当前节点就是 LCA；
若 root.val 比 val1 还小，则需要去值更大的右子树寻找 LCA；
若 root.val 比 val2 还大，则需要去值更小的左子树寻找 LCA。
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 保证 val1 较小，val2 较大
        val1 = min(p.val, q.val)
        val2 = max(p.val, q.val)
        return self.find(root, val1, val2)

    # 在 BST 中寻找 val1 和 val2 的最近公共祖先节点
    def find(self, root: 'TreeNode', val1: int, val2: int) -> 'TreeNode':
        if root is None:
            return None
        if root.val > val2:
            # 当前节点太大，去左子树找
            return self.find(root.left, val1, val2)
        if root.val < val1:
            # 当前节点太小，去右子树找
            return self.find(root.right, val1, val2)
        # val1 <= root.val <= val2
        # 则当前节点就是最近公共祖先
        return root