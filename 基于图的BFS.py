"""
图结构的广度优先搜索其实就是 多叉树的层序遍历，无非就是加了一个 visited 数组来避免重复遍历节点。

理论上 BFS 遍历也需要区分遍历所有「节点」和遍历所有「路径」，但是实际上 BFS 算法一般只用来寻找那条最短路径，不会用来求所有路径。

"""
from utils import *
# 加权有向图的通用实现（邻接表）
class WeightedDigraph:
    
    # 存储相邻节点及边的权重
    class Edge:
        def __init__(self, to: int, weight: int):
            self.to = to
            self.weight = weight

    def __init__(self, n: int):
        # 我们这里简单起见，建图时要传入节点总数，这其实可以优化
        # 比如把 graph 设置为 Map<Integer, List<Edge>>，就可以动态添加新节点了
        self.graph = [[] for _ in range(n)]

    # 增，添加一条带权重的有向边，复杂度 O(1)
    def addEdge(self, from_: int, to: int, weight: int):
        self.graph[from_].append(self.Edge(to, weight))

    # 删，删除一条有向边，复杂度 O(V)
    def removeEdge(self, from_: int, to: int):
        self.graph[from_] = [e for e in self.graph[from_] if e.to != to]

    # 查，判断两个节点是否相邻，复杂度 O(V)
    def hasEdge(self, from_: int, to: int) -> bool:
        for e in self.graph[from_]:
            if e.to == to:
                return True
        return False

    # 查，返回一条边的权重，复杂度 O(V)
    def weight(self, from_: int, to: int) -> int:
        for e in self.graph[from_]:
            if e.to == to:
                return e.weight
        raise ValueError("No such edge")
    
    # 上面的 hasEdge、removeEdge、weight 方法遍历 List 的行为是可以优化的
    # 比如用 Map<Integer, Map<Integer, Integer>> 存储邻接表
    # 这样就可以避免遍历 List，复杂度就能降到 O(1)

    # 查，返回某个节点的所有邻居节点，复杂度 O(1)
    def neighbors(self, v: int):
        return self.graph[v]


# 图结构的 BFS 遍历，从节点 s 开始进行 BFS
"""
写法1：对应前面层序遍历写法1

from collections import deque

def level_order_traverse(root):
    if root is None:
        return

    q = deque()
    q.append(root)
    
    while q:
        cur = q.popleft()
        # 访问 cur 节点
        print(cur.val)
        
        # 把 cur 的所有子节点加入队列
        for child in cur.children:
            q.append(child)

#### #### #### #### #### #### 
#### 注意跟DFS可以对比一下: #### 
#### #### #### #### #### #### 

| 遍历方式    | 数据结构     | 入节点顺序 | 出节点顺序 | 效果                |
| ---------- | ---------- | -------- | --------- | ------------------ |
| DFS（前序） | 栈（LIFO）   | 先右后左  | 先左后右   | 深度优先，从根一路往下 |
| BFS（层序） | 队列（FIFO） | 先左后右  | 先左后右   | 广度优先，一层一层遍历 |

# 栈迭代写法
def preorder_iter(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            print(node.val)
            stack.append(node.right)
            stack.append(node.left)

# 递归写法
def preorder(node):
    if not node:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)

"""
from collections import deque
def bfs(graph, s):
    visited = [False] * len(graph) # self.graph = [[] for _ in range(n)] 即点i...n指向哪些点
    from collections import deque
    q = deque([s])
    visited[s] = True
    # while q:
    #     print("开始：",q)
    #     sz = len(q)
    #     for _ in range(sz):
    #         cur = q.popleft()
    #         print("pop:",cur, q)
    #         print([e.to for e in graph.neighbors(cur)])
    #         for e in graph.neighbors(cur):
                
    #             if visited[e.to]: 
    #                 print("visited：",e.to)
    #                 continue
    #             print("not visited：",e.to)
                
    #             q.append(e.to)
    #             visited[e.to] = True
    #             print("visited:",visited)
    #         print("- "*10)
    #     print("*"*25)

    while q:
        cur = q.popleft() #cur是点的index，是个数字
        print(f"visit {cur}")
        for e in graph.neighbors(cur):
            if visited[e.to]: 
                continue
            q.append(e.to)
            visited[e.to] = True




"""
写法2：对应前面层序遍历写法2
from collections import deque

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
"""
from collections import deque

# 从 s 开始 BFS 遍历图的所有节点，且记录遍历的步数
def bfs2(graph, s):
    visited = [False] * len(graph)   ##
    q = deque([s])
    visited[s] = True                ##
    # 记录从 s 开始走到当前节点的步数 
    step = 0
    
    while q:
        sz = len(q)
        for i in range(sz):
            cur = q.popleft()
            print(f"visit {cur} at step {step}")
            for e in graph.neighbors(cur):
                if visited[e.to]:    ##
                    continue         ##
                q.append(e.to)       ##
                visited[e.to] = True ##
        step += 1





"""
写法3：对应前面层序遍历写法3
# 多叉树的层序遍历
# 每个节点自行维护 State 类，记录深度等信息
class State:
    def __init__(self, node, depth):
        self.node = node
        self.depth = depth

def levelOrderTraverse(root):
    if root is None:
        return
    q = deque()
    # 记录当前遍历到的层数（根节点视为第 1 层）
    q.append(State(root, 1))

    while q:
        state = q.popleft()
        cur = state.node
        depth = state.depth
        # 访问 cur 节点，同时知道它所在的层数
        print(f"depth = {depth}, val = {cur.val}")

        for child in cur.children:
            q.append(State(child, depth + 1))
"""
# 图结构的 BFS 遍历，从节点 s 开始进行 BFS，且记录遍历步数（从起点 s 到当前节点的边的条数）
# 每个节点自行维护 State 类，记录从 s 走来的遍历步数
class State:
    def __init__(self, node, step):
        # 当前节点 ID
        self.node = node
        # 从起点 s 到当前节点的遍历步数
        self.step = step


def bfs3(graph, s):
    visited = [False] * len(graph)  ##
    from collections import deque

    q = deque([State(s, 0)])
    visited[s] = True ##

    while q:
        state = q.popleft()
        cur = state.node
        step = state.step  ##
        print(f"visit {cur} with step {step}")
        for e in graph.neighbors(cur):
            if visited[e.to]:  
                continue
            q.append(State(e.to, step + 1)) 
            visited[e.to] = True



# 测试用例
if __name__ == "__main__":
    # 建立一个加权有向图，5 个节点（0 到 4）
    graph = WeightedDigraph(5)
    graph.addEdge(0, 1, 1)
    graph.addEdge(0, 2, 1)
    graph.addEdge(4, 3, 4)
    graph.addEdge(0, 4, 4)
    graph.addEdge(1, 4, 0)
    graph.addEdge(1, 2, 1)
    graph.addEdge(2, 4, 1)
    graph.addEdge(2, 3, 1)
    for i in range(4):
        cur = i
        print(i)
        for e in graph.neighbors(cur):
            print(i, e.to)

    
    
    print('BFS')
    print("BFS starting from node 0:")
    bfs1(graph, 0)
    draw_weighted_digraph(graph)

