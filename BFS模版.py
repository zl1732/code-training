"""
DFS/回溯算法的本质就是递归遍历一棵穷举树（多叉树），而多叉树的递归遍历又是从二叉树的递归遍历衍生出来的。所以我说 DFS/回溯算法的本质是二叉树的递归遍历。
BFS 算法的本质就是遍历一幅图
"""

"""
BFS 算法框架 就是从二叉树的层序遍历扩展出来的，常用于求无权图的最短路径问题。
111. 二叉树的最小深度 | 力扣 | LeetCode |  🟢

##############
# 普通dfs 遍历所有树枝
##############
class Solution:
    def __init__(self):
        self.minDepthValue = float('inf')
        self.currentDepth = 0

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.traverse(root)
        return self.minDepthValue

    def traverse(self, root: TreeNode) -> None:
        if root is None:
            return
        # 前序位置进入节点时增加当前深度
        self.currentDepth += 1
        # 如果当前节点是叶子节点，更新最小深度
        if root.left is None and root.right is None:
            self.minDepthValue = min(self.minDepthValue, self.currentDepth)
        self.traverse(root.left)
        self.traverse(root.right)
        # 后序位置离开节点时减少当前深度
        self.currentDepth -= 1


##############
# bfs 走到第一个叶子
##############
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
"""

"""
找全部路径通常使用DFS。为什么不好用BFS？？需要额外记录

from collections import deque
# 定义 State 类
class State:
    def __init__(self, node, path):
        self.node = node  # 当前节点
        self.path = path  # 到达当前节点的路径

# BFS 层序遍历
def levelOrderTraverse(root):
    if root is None:
        return
    
    q = deque()
    # 根节点的路径是根本的路径
    q.append(State(root, [root.val]))

    while q:
        cur = q.popleft()  # 弹出队列中的元素
        
        # 访问当前节点，打印路径
        print(f"Node: {cur.node.val}, Path: {cur.path}")

        # 如果当前节点有左子节点
        if cur.node.left is not None:
            # 构建新路径并加入队列
            new_path = cur.path + [cur.node.left.val]
            q.append(State(cur.node.left, new_path))
        
        # 如果当前节点有右子节点
        if cur.node.right is not None:
            # 构建新路径并加入队列
            new_path = cur.path + [cur.node.right.val]
            q.append(State(cur.node.right, new_path))

"""

"""
比方说给你一个迷宫游戏，请你计算走到出口的最小步数？如果这个迷宫还包含传送门，可以瞬间传送到另一个位置，那么最小步数又是多少？
再比如说两个单词，要求你通过某些替换，把其中一个变成另一个，每次可以替换/删除/插入一个字符，最少要操作几次？
再比如说连连看游戏，两个方块消除的条件不仅仅是图案相同，还得保证两个方块之间的最短连线不能多于两个拐点。你玩连连看，点击两个坐标，游戏是如何判断它俩的最短连线有几个拐点的？
"""




### 算法框架
## 参考《基于图的BFS.py》三种写法
    # 第一种写法最简单，但局限性太大，不常用；
    # 第二种写法最常用，中等难度的 BFS 算法题基本都可以用这种写法解决；
    # 第三种写法稍微复杂一点，但灵活性最高，可能会在一些难度较大的的 BFS 问题中用到。


## 第二种写法

#备注
"""
层序遍历写法2
def levelOrderTraverse(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    # 记录当前遍历到的层数（根节点视为第 1 层）
    depth = 1

    while q:
        sz = len(q)
        for i in range(sz):
            cur = q.popleft()
            # 访问 cur 节点，同时知道它所在的层数
            print(f"depth = {depth}, val = {cur.val}")

            for child in cur.children:
                q.append(child)
        depth += 1

图BFS写法2
def bfs(graph, s):
    visited = [False] * len(graph)                  ++
    q = deque([s])
    visited[s] = True                               ++
    # 记录从 s 开始走到当前节点的步数
    step = 0
    
    while q:
        sz = len(q)
        for i in range(sz):
            cur = q.popleft()
            print(f"visit {cur} at step {step}")
            for e in graph.neighbors(cur):
                if visited[e.to]:                   ++
                    continue                        ++
                q.append(e.to)                      ++
                visited[e.to] = True                ++
        step += 1
"""

# 算法框架2: 带找target
def bfs(graph, s, target):
    visited = [False] * len(graph)
    q = deque([s])
    visited[s] = True
    step = 0
    
    while q:
        sz = len(q)
        for i in range(sz):
            cur = q.popleft()
            print(f"visit {cur} at step {step}")
            # 找到
            if cur == target:                      #++#
                return step                        #++#

            # 向邻居扩散搜索
            for to in neighborsOf(cur):
                if not visited[to]:
                    q.append(to)
                    visited[to] = True
        """
        BFS 的 step 含义：从起点 s 到当前“层”的距离。注意上面depth += 1的位置
        step = 0：起点所在层
        step = 1：起点的邻居
        step = 2：邻居的邻居

        for i in range(sz) 的作用：
        保证这一层的 所有节点 都在 step 这个距离内被访问。
        所以要等这一层的节点都访问完，再统一做 step += 1，表示“进入下一层”。

        情况 2：step += 1 在 for 内层 ❌
            就会变成 访问一个节点就加一步。
            step = 已访问的节点数（相当于全局计数器）。
            不再是“最短路径步数”，而是“到目前为止访问了多少节点”。
        """
        step += 1
    # 没找到
    return -1                                      #++#





# 力扣第 773 题「滑动谜题
"""
其实棋盘的初始状态就可以认为是起点：
[[2,4,1],
 [5,0,3]]

我们最终的目标状态是把棋盘变成这样：
[[1,2,3],
 [4,5,0]]

抽象出来的图结构也是会包含环的，所以需要一个 visited 数组记录已经走过的节点，避免成环导致死循环。
(也就是一个块来回移动)

注意：二维数组这种可变数据结构是无法直接加入哈希集合的。
     常见的解决方案是把二维数组序列化成一个字符串，这样就可以直接存入哈希集合了。    

# 记录一维字符串的相邻索引
重要！！！！
    0 1 2 3 4 5这里实际上是棋盘位置的index，映射的集合也是index，不管什么数只要在这个位置就可以和映射集合里的index位置交换
    🔁 不管棋盘内容怎么变，mapping 永远有效
    你不关心位置上是 1、2、3、4、5 还是 0；
    你只看位置编号：格子 0 可以去 1 和 3，格子 4 可以去 1、3、5；
    所以只需要 mapping 就能控制滑动规则。

[[0,1,2],
 [3,4,5]]
neighbor = [
    [1, 3],      # 0 能换到右边的 1，下面的 3
    [0, 4, 2],   # 1 能换到左边的 0，右边的 2，下面的 4
    [1, 5],      # 2 能换到左边的 1，下面的 5
    [0, 4],      # 3 能换到上边的 0，右边的 4
    [3, 1, 5],   # 4 能换到左边的 3，上边的 1，右边的 5
    [4, 2]       # 5 能换到左边的 4，上边的 2
]
neighbor[0] = [1,3]
"""

from collections import deque

class Solution:
    def slidingPuzzle(self, board):
        target = "123450"
        # 将 2x3 的数组转化成字符串作为 BFS 的起点
        # [[2,4,1],
        # [5,0,3]] -> "241503"
        start = ""
        """
        注意：
        range(len(board))
        += str(board[i][j])
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                start += str(board[i][j])
        
        # ****** BFS 算法框架开始 ******
        q = deque()
        visited = set()
        q.append(start)
        visited.add(start)  # visit记录的是一个个字符串，这里用set因为不好用多维数组
        
        step = 0
        while q: 
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                # 判断是否达到目标局面
                if cur == target:
                    return step
                # 将数字 0 和相邻的数字交换位置
                for neighbor_board in self.getNeighbors(cur):
                    # 防止走回头路
                    if neighbor_board not in visited:
                        q.append(neighbor_board)
                        visited.add(neighbor_board)
            step += 1
        # ****** BFS 算法框架结束 ******
        return -1


    def getNeighbors(self, board):
        """board就是字符串"""
        # 记录一维字符串的相邻索引
        mapping = [
            [1, 3],
            [0, 4, 2],
            [1, 5],
            [0, 4],
            [3, 1, 5],
            [4, 2]
        ] 
        
        # 因为要把0和其他数交换，所以先找到0的index
        """
        注意：index('0')
        """
        idx = board.index('0')
        neighbors = []
        for adj in mapping[idx]:
            """swap需要输入字符串"""
            new_board = self.swap(board, idx, adj) 
            neighbors.append(new_board)
        return neighbors

    def swap(self, board, i, j):
        chars = list(board)          # 字符串转成数组，方便交换
        chars[i], chars[j] = chars[j], chars[i]
        return ''.join(chars)        # 再转回字符串
    


# 自己写
class Solution:
    def slidingPuzzle(self, board):
        target = "123450"
        start = ""
        # 生成start子串
        # for i in len(board):
        #     for j in len(board[0]):
        #         start.append(board[i][j])
        for i in range(len(board)):
            for j in range(len(board[0])):
                start += str(board[i][j])
        
        q = deque([start])
        visited = set()
        visited.add(start)
        step = 0

        while q:
            sz = len(q)
            for i in range(sz):
                board = q.popleft()
                if board == target:
                    return step
                
                for neighbor in self.getNeighbors(board):
                    if neighbor in visited:
                        continue
                    q.append(neighbor)
                    visited.add(neighbor)
            step += 1
        return -1
    
    def getNeighbors(self, board):
        # [0,1,2]
        # [3,4,5]
        mapping = {0:[1,3],
                   1:[0,4,2],
                   2:[1,5],
                   3:[0,4],
                   4:[3,1,5],
                   5:[4,2]}
        # 只换0，所以找0的位置
        # idx = board.index(0) 
        idx = board.index("0") 
        neighbors = []
        for adj in mapping[idx]:
            string = self.swap(board, adj, idx)
            neighbors.append(string)
        return neighbors

    def swap(self, board, adj, idx):
        # 首先变list
        chars = list(board)
        chars[adj],chars[idx] = chars[idx],chars[adj]
        return ''.join(chars)
    

