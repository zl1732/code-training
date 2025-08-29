#297. Serialize and Deserialize Binary Tree
from typing import List

"""
我们先思考一个问题：

什么样的序列化的数据可以反序列化出唯一的一棵二叉树？
给你一棵二叉树的前序遍历结果，你是否能够根据这个结果还原出这棵二叉树呢？
   
答案是也许可以，也许不可以，
    具体要看你给的前序遍历结果是否包含空指针的信息。
    如果包含了空指针，那么就可以唯一确定一棵二叉树，否则就不行。
因为前序/后序遍历的结果中，可以确定根节点的位置，而中序遍历的结果中，根节点的位置是无法确定的。
"""


"""
前序：序列化
"""
class Codec:
    SEP = ","
    NULL = "#"

    # 主函数，将二叉树序列化为字符串
    def serialize(self, root):
        # string builder，没有写作self.sb
        sb = []
        self._serialize(root, sb)
        return "".join(sb)

    # 辅助函数，将二叉树存入 StringBuilder
    def _serialize(self, root, sb):
        if root is None:
            sb.append(self.NULL)
            sb.append(self.SEP)
            return

        # ****** 前序位置 ********
        sb.append(str(root.val))
        sb.append(self.SEP)
        # ***********************

        self._serialize(root.left, sb)
        self._serialize(root.right, sb)





"""
前序：反序列化
不会出现右子节点被错误放到 root.left 的问题，顺序总是对的。
    这是因为节点列表是前序遍历的顺序，每次递归处理的节点就是当前子树的根节点，处理顺序严格是：
    根 → 左子树 → 右子树
    所以每次调用 self._deserialize(nodes) 时，nodes 的顺序本身已经安排好了下一个是左，之后是右。
nodes 已经是有序的前序遍历结果（含 null）
"""
class Codec:
    SEP = ","
    NULL = "#"

    # 主函数，将字符串反序列化为二叉树结构
    def deserialize(self, data: str):
        # 将字符串转化成列表
        nodes = data.split(self.SEP)
        return self._deserialize(nodes)

    # 辅助函数，通过 nodes 列表构造二叉树
    """
    注意是分解思路
    | 判断逻辑                  | 场景说明                                 | 是否必须 |
    | ------------------------ | ---------------------------            | ---- |
    | `if not nodes:`          | 避免访问空列表导致 `pop(0)` 报错（索引越界） | ✅ 必须 |
    | `if first == self.NULL:` | 当前节点是 null，占位符，表示这棵子树是空的   | ✅ 必须 |

    ① if not nodes: return None
        作用是提前终止，防止你对空列表执行 pop(0)

    ② if first == self.NULL: return None
    这是逻辑层面的判断：
        "#" 是我们序列化时表示空指针的标记。
        它代表一棵“空树”或空子树，即当前递归的这个位置上，不存在真实节点。
    """
    def _deserialize(self, nodes: List[str]):
        """
        🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
            return None  ✅ 明确返回 None
            return       ⚠️ 隐式返回 None（但不推荐这样用）
            ⚠️ return（裸写）
            等价于 return None，因为 Python 默认函数无返回值就是 None
            但别人读代码时，可能一眼看不出你是要返回 None，还是你忘了写值
            可读性更差，尤其在多重 return 场景中不清晰
        🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
        """
        if not nodes: return None

        # ****** 前序位置 *******
        # 列表最左侧就是根节点
        first = nodes.pop(0)
        if first == self.NULL: 
            return None
        root = TreeNode(int(first)) 
        # *********************

        """
        利用了list 的可变性
        ❓那改成全局变量会更好吗？

            答案是：
            ❌ 不建议改成全局变量，除非有明确理由。
            ✅ 当前的「作为参数传入引用」方式其实是最清晰、安全、通用的做法。
        """
        root.left = self._deserialize(nodes)
        root.right = self._deserialize(nodes)

        return root
    

class Codec:
    SEP = ","
    NULL = "#"

    def deserialize(self, data: str):
        if not data:
            return None
        nodes = data.split(self.SEP)
        return self._deserialize(nodes)

    def _deserialize(self, nodes: List[str]):
        if not nodes:
            return None
        
        val = nodes.pop(0)
        if val == self.NULL:
            return None
        root = TreeNode(val)
        # 注意这里是先构造左子树，后构造右子树
        root.left = self._deserialize(nodes)
        root.right = self._deserialize(nodes)
        return root


        

        
        
        



"""
后序：序列化
"""
# 辅助函数，将二叉树存入 StringBuilder
def _serialize(root, sb):
    if root is None:
        """
        反序列化的时候可以安全忽略末尾空字符串
        后序遍历顺序是：2,#,#,3,#,#,1,
        """
        sb.append(NULL).append(SEP)
        return

    _serialize(root.left, sb)
    _serialize(root.right, sb)
    
    # ****** 后序位置 ********
    sb.append(root.val).append(SEP)
    # ***********************






"""
后序：反序列化
"""
"""
1. 典型错误：显然上述代码是错误的，变量都没声明呢，就开始用了
"""
# 辅助函数，通过 nodes 列表构造二叉树
def deserialize(nodes):
    if not nodes:
       return None

    root.left = deserialize(nodes)
    root.right = deserialize(nodes)

    # 后序位置
    first = nodes.pop(0)
    if first == 'NULL':
        return None
    root = TreeNode(int(first))

    return root

"""
正确：要先构造 root.right 子树，后构造 root.left 子树。
"""
class Codec:
    SEP = ","
    NULL = "#"
    # 主函数，将字符串反序列化为二叉树结构
    def deserialize(self, data):
        # 将分割结果中的空字符串过滤掉
        "注意要过滤空字符，直接用 if x"
        nodes = [x for x in data.split(self.SEP) if x]
        return self._deserialize(nodes)

    # 辅助函数，通过 nodes 列表构造二叉树
    def _deserialize(self, nodes):
        if nodes == []:
            return None
        "注意后序，是反着排列，可能是切了，出现“”"
        "命名用last，对应前面first"
        # 从后往前取出元素
        last = nodes.pop() 
        if last == self.NULL or last == "":
            return None
        root = TreeNode(int(last))
        # 先构造右子树，后构造左子树
        root.right = self._deserialize(nodes)
        root.left = self._deserialize(nodes)
        return root




"""
中序：序列化
"""
# 辅助函数，将二叉树存入 StringBuilder
def serialize(root: 'TreeNode', sb: 'List[str]') -> None:
    if root == None:
        sb.append(NULL)
        sb.append(SEP)
        return

    serialize(root.left, sb)
    # ******* 中序位置 *******
    sb.append(str(root.val))
    sb.append(SEP)
    # ***********************
    serialize(root.right, sb)



"""
层序遍历
"""
# 之前学的标准写法：
# 可以看到，队列 q 中不会存在 null 指针。
def traverse(root):
    if root is None:
        return
    # 初始化队列，将 root 加入队列
    q = [root]
    
    while q:
        sz = len(q)
        for i in range(sz):
            # 层级遍历代码位置
            cur = q.pop(0)  ## pop(0) 从列表头部（左边）取出
            print(cur.val)
            # *************
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)


" 把对空指针的检验从「将元素加入队列」的时候改成了「从队列取出元素」的时候。"
" 观察代码结构的改变即可，主要是判断none的位置"

from collections import deque
def traverse(root):
    if not root: 
        return
    # 初始化队列，将 root 加入队列
    q = deque([root])

    while q:
        sz = len(q)
        for _ in range(sz):
            cur = q.popleft()
            # 层级遍历代码位置
            if cur is None:       #
                continue
            print(cur.val)
            # **************

            q.append(cur.left)    #
            q.append(cur.right)   #




"层级遍历 序列化"
class Codec:
    SEP = ","
    NULL = "#"

    # 将二叉树序列化为字符串
    def serialize(self, root):
        if root is None:
            return ""
        # 初始化队列，将 root 加入队列
        queue = [root]
        res = []
        while queue:
            sz = len(queue)
            for i in range(sz):
                cur = queue.pop(0)

                # 层级遍历代码位置
                if cur is None:
                    res.append(self.NULL)
                    res.append(self.SEP)
                    continue
                res.append(str(cur.val))
                res.append(self.SEP)
                # ***************

                queue.append(cur.left)
                queue.append(cur.right)

        return Codec.SEP.join(res)
    




"层级遍历 反序列化"
from collections import deque
class Codec:
    SEP = ","
    NULL = "#"

    # 将字符串反序列化为二叉树结构
    def deserialize(self, data: str):
        if data == "":
            return None
        # 将分割结果中的空字符串过滤掉
        nodes = [x for x in data.split(self.SEP) if x]
        # 第一个元素就是 root 的值
        root = TreeNode(int(nodes[0]))
        # 队列 q 记录父节点，将 root 加入队列
        q = deque([root])

        # index 变量记录正在序列化的节点在数组中的位置
        index = 1
        while q:
            sz = len(q)
            for i in range(sz):
                parent = q.popleft()
                # 为父节点构造左侧子节点
                left = nodes[index]
                index += 1
                """
                ❌ 错误方式：不判断直接构建
                # 即便是"#"，也创建了节点
                parent.right = TreeNode(right)
                如果 right == "#", 就会构造出一个奇怪的 TreeNode("#")，你后续遍历会遍历到这个不该存在的节点。
                你不得不在很多地方写：
                if node.val == "#":
                    continue  # 或 return
                这种方式违反了我们构建“干净树结构”的目标。

                叶子节点不用指向None，会自动指向
                """
                if left != self.NULL:
                    parent.left = TreeNode(int(left))
                    q.append(parent.left)
                # 为父节点构造右侧子节点
                right = nodes[index]
                index += 1
                if right != self.NULL:
                    parent.right = TreeNode(int(right))
                    q.append(parent.right)
                    
        return root
    

    # 将字符串反序列化为二叉树结构
    def deserialize(self, data: str):
        if data == "":
            return None
        nodes = [x for x in data.split(self.SEP) if x]
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        index = 1

        while q:
            sz = len(q)
            for i in range(sz):
                parent = q.popleft()
                left = nodes[index]
                index += 1
                if left != self.NULL:
                    parent.left = TreeNode(int(left))
                    q.append(parent.left)
                right = nodes[index]
                index += 1
                if right != self.NULL:
                    parent.right = TreeNode(int(right))
                    q.append(parent.right)
        return root
    
    # 将字符串反序列化为二叉树结构
    def deserialize_right(self, data: str):
        if data == "":
            return None
        nodes = [x for x in data.split(self.SEP) if x]
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        index = 1

        while q:
            sz = len(q)
            for i in range(sz):
                parent = q.popleft()
                if index < len(nodes):
                    left = nodes[index]
                    index += 1
                    if left != self.NULL:
                        parent.left = TreeNode(int(left))
                        q.append(parent.left)
                if index < len(nodes):
                    right = nodes[index]
                    index += 1
                    if right != self.NULL:
                        parent.right = TreeNode(int(right))
                        q.append(parent.right)
        return root
    

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(root):
    if root is None:
        return "None"
    return f"{root.val} -> ({print_tree(root.left)}, {print_tree(root.right)})"

c = Codec()
# 序列化
data = "1,2,#,#,3,4,#,#,5,#,#"
data = "1,2,#"
# root = c.deserialize(data)
root2 = c.deserialize_right(data)
print("反序列化结果:", print_tree(root2))

"""
我们来执行一下：
    初始：
        nodes = ["1", "2", "#"]
        index = 1
        队列：[1]
    第一次循环：
        parent = TreeNode(1)
        left = nodes[1] = "2" → ok，创建 TreeNode(2)，入队
        index = 2
        right = nodes[2] = "#" → ok，跳过右子树
        index = 3 ✅
    下一轮循环开始时：
        队列里还有 TreeNode(2)，需要处理它的左右子节点
        你会进入下一次 parent = TreeNode(2)
        接着：
left = nodes[index]   # index = 3
Boom 💥 IndexError：列表越界
你的数据 "1,2,#"，只给了一个左孩子和一个右空，却没给 2 的任何孩子信息，于是当 2 出队，程序去取它的左子时，index = 3，就炸了。
"""

# 前序递归反序列化
class Codec:
    SEP = ","
    NULL = "#"

    def deserialize(self, data: str):
        if not data:
            return None
        nodes = data.split(self.SEP)
        return self._deserialize(nodes)

    def _deserialize(self, nodes: List[str]):
        """
        ❌ 但它并不会负责检查是否“刚好用完”所有节点
        """
        if not nodes:
            return None
        
        val = nodes.pop(0)
        if val == self.NULL:
            return None
        root = TreeNode(val)
        # 注意这里是先构造左子树，后构造右子树
        root.left = self._deserialize(nodes)
        root.right = self._deserialize(nodes)
        return root
    
