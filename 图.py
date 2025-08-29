
import matplotlib.pyplot as plt
import networkx as nx

"""
# 邻接表
"""
def draw_weighted_digraph(g):
    G = nx.DiGraph()
    
    # 添加边及权重
    for u in range(len(g.graph)):  # 假设 g.graph 是邻接表：List[List[Edge]]
        for e in g.graph[u]:
            G.add_edge(u, e.to, weight=e.weight)

    # 使用 spring 布局绘图
    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000,
            arrows=True, arrowstyle='-|>', arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Directed Weighted Graph")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

"""
# 遍历邻接矩阵构建 NetworkX 图
"""

def draw_weighted_digraph1(g: WeightedDigraph1):
    G = nx.DiGraph()
    n = len(g.matrix)

    # 遍历邻接矩阵构建 NetworkX 图
    for u in range(n):
        for v in range(n):
            if g.matrix[u][v] > 0:
                G.add_edge(u, v, weight=g.matrix[u][v])

    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000,
            arrows=True, arrowstyle='-|>', arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Directed Weighted Graph (Adjacency Matrix)")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

###########################################################################

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

if __name__ == "__main__":
    graph = WeightedDigraph(3)
    graph.addEdge(0, 1, 1)
    graph.addEdge(1, 2, 2)
    graph.addEdge(2, 0, 3)
    graph.addEdge(2, 1, 4)

    print(graph.hasEdge(0, 1))  # true
    print(graph.hasEdge(1, 0))  # false

    for edge in graph.neighbors(2):
        print(f"{2} -> {edge.to}, weight: {edge.weight}")
    # 2 -> 0, weight: 3
    # 2 -> 1, weight: 4

    graph.removeEdge(0, 1)
    print(graph.hasEdge(0, 1))  # false
    print(graph.graph)





# """
# ✅ 优化版：使用字典提高效率
# 和临近矩阵版本其实还是不一样：
# ✅ 邻接矩阵用的是 O(n²) 空间（即使图很稀疏，也要存下每对点的状态）
# ✅ 邻接表 + dict 是只为实际存在的边分配内存

# | 特点              | 邻接矩阵（`List[List[int]]`） | 邻接表 + dict（我优化后的实现） |
# | --------------- | ----------------------- | ------------------- |
# | 是否稀疏图适用         | ❌ 不适合稀疏图，空间浪费严重         | ✅ 特别适合稀疏图           |
# | 空间复杂度           | O(n²)                   | O(n + m)，其中 m 是边数   |
# | 插入边             | O(1)                    | O(1)                |
# | 删除边             | O(1)                    | O(1)                |
# | 查询是否有边（hasEdge） | O(1)                    | O(1)                |
# | 遍历某节点的邻居        | O(n)（要遍历整行）             | O(k)，k 是出边数量        |
# ✅ 邻接表 + dict 是稀疏图最优解
# ❌ 邻接矩阵是稠密图才合适
# """
# class WeightedDigraphFast:
#     def __init__(self, n: int):
#         # 每个节点维护一个字典：{to: weight}
#         self.graph = [{} for _ in range(n)]

#     # 添加边，复杂度 O(1)
#     def addEdge(self, from_: int, to: int, weight: int):
#         self.graph[from_][to] = weight

#     # 删除边，复杂度 O(1)
#     def removeEdge(self, from_: int, to: int):
#         self.graph[from_].pop(to, None)

#     # 判断是否有边，复杂度 O(1)
#     def hasEdge(self, from_: int, to: int) -> bool:
#         return to in self.graph[from_]

#     # 获取权重，复杂度 O(1)
#     def weight(self, from_: int, to: int) -> int:
#         if to in self.graph[from_]:
#             return self.graph[from_][to]
#         raise ValueError("No such edge")

#     # 获取所有邻居（返回 [(to, weight), ...]），复杂度 O(k)
#     def neighbors(self, v: int):
#         return list(self.graph[v].items())


"""
基于图的dfs遍历
    * WeightedDigraph
    * WeightedUndigraph（底层用的是 WeightedDigraph）

"""
# DFS 遍历所有点
def traverse(graph: WeightedDigraph, s: int, visited: list):
    # base case
    if s < 0 or s >= len(graph.graph):  # 注意这里访问 graph.graph，而不是 graph 本身
        return
    if visited[s]:
        # 防止死循环
        return
    # 前序位置
    visited[s] = True
    print("visit", s)
    for e in graph.neighbors(s):
        traverse(graph, e.to, visited)
    # 后序位置

# 遍历所有边（二维 visited 数组）
# 从起点 s 开始遍历图的所有边
"""
显然，使用二维 visited 数组并不是一个很高效的实现方式，因为需要创建二维 visited 数组，这个算法的时间复杂度是 O(E+V2)O(E+V2)，空间复杂度是 O(V2)O(V2)，其中 EE 是边的数量，VV 是节点的数量。

在讲解 Hierholzer 算法计算欧拉路径 时，我们会介绍一种简单的优化避免使用二维 visited 数组，这里暂不展开。

"""
def traverse_edges(graph, s, visited):
    # base case
    if s < 0 or s >= len(graph.graph):
        return
    for e in graph.neighbors(s):
        # 如果边已经被遍历过，则跳过
        if visited[s][e.to]:
            continue
        # 标记并访问边
        visited[s][e.to] = True
        print(f"visit edge: {s} -> {e.to}")
        print(visited)
        traverse_edges(graph, e.to, visited)

# 测试用例
if __name__ == "__main__":
    # 建立一个加权有向图，5 个节点（0 到 4）
    g = WeightedDigraph(5)
    g.addEdge(0, 1, 3)
    g.addEdge(0, 2, 5)
    g.addEdge(1, 2, 2)
    g.addEdge(2, 0, 1)
    g.addEdge(2, 3, 4)
    g.addEdge(3, 4, 6)
    g.addEdge(4, 1, 7)  # 构成一个环：1 → 2 → 3 → 4 → 1
    # 画图
    draw_weighted_digraph(g)
    
    print('DFS')
    # DFS
    visited = [False] * 5
    print("DFS starting from node 0:")
    traverse(g, 0, visited)

    # DFS边
    visited = [[False] * 5 for _ in range(5)]
    traverse_edges(g, 0, visited)


###########################################################################

"""
有向加权图（邻接矩阵实现）
"""
class WeightedDigraph1:
    # 存储相邻节点及边的权重
    class Edge:
        def __init__(self, to, weight):
            self.to = to
            self.weight = weight

    def __init__(self, n):
        # 邻接矩阵，matrix[from][to] 存储从节点 from 到节点 to 的边的权重
        # 0 表示没有连接
        self.matrix = [[0] * n for _ in range(n)]

    # 增，添加一条带权重的有向边，复杂度 O(1)
    def addEdge(self, from_node, to, weight):
        self.matrix[from_node][to] = weight

    # 删，删除一条有向边，复杂度 O(1)
    def removeEdge(self, from_node, to):
        self.matrix[from_node][to] = 0

    # 查，判断两个节点是否相邻，复杂度 O(1)
    def hasEdge(self, from_node, to):
        return self.matrix[from_node][to] != 0

    # 查，返回一条边的权重，复杂度 O(1)
    def weight(self, from_node, to):
        return self.matrix[from_node][to]

    # 查，返回某个节点的所有邻居节点，复杂度 O(V)
    def neighbors(self, v):
        res = []
        for i in range(len(self.matrix[v])):
            if self.matrix[v][i] > 0:
                res.append(self.Edge(i, self.matrix[v][i]))
        return res


def traverse(graph: WeightedDigraph1, s: int, visited: list):
    if s < 0 or s >= len(graph.matrix):
        return
    if visited[s]:
        return
    visited[s] = True
    print("visit", s)
    for e in graph.neighbors(s):
        traverse(graph, e.to, visited)


if __name__ == "__main__":
    g = WeightedDigraph1(5)
    g.addEdge(0, 1, 3)
    g.addEdge(0, 2, 5)
    g.addEdge(1, 2, 2)
    g.addEdge(2, 0, 1)
    g.addEdge(2, 3, 4)
    g.addEdge(3, 4, 6)
    g.addEdge(4, 1, 7)

    # DFS
    print('DFS')
    visited = [False] * 5
    print("DFS starting from node 0:")
    traverse(g, 1, visited)

    print(graph.hasEdge(0, 1)) # True
    print(graph.hasEdge(1, 0)) # False

    for edge in graph.neighbors(2):
        print(f"{2} -> {edge.to}, weight: {edge.weight}")
    # 2 -> 0, weight: 3
    # 2 -> 1, weight: 4

    graph.removeEdge(0, 1)
    print(graph.hasEdge(0, 1)) # False


###########################################################################

# 无向加权图的通用实现
class WeightedUndigraph:
    def __init__(self, n):
        self.graph = WeightedDigraph(n)

    # 增，添加一条带权重的无向边
    def addEdge(self, frm, to, weight):
        self.graph.addEdge(frm, to, weight)
        self.graph.addEdge(to, frm, weight)

    # 删，删除一条无向边
    def removeEdge(self, frm, to):
        self.graph.removeEdge(frm, to)
        self.graph.removeEdge(to, frm)

    # 查，判断两个节点是否相邻
    def hasEdge(self, frm, to):
        return self.graph.hasEdge(frm, to)

    # 查，返回一条边的权重
    def weight(self, frm, to):
        return self.graph.weight(frm, to)

    # 查，返回某个节点的所有邻居节点
    def neighbors(self, v):
        return self.graph.neighbors(v)

if __name__ == "__main__":
    graph = WeightedUndigraph(3)
    graph.addEdge(0, 1, 1)
    graph.addEdge(1, 2, 2)
    graph.addEdge(2, 0, 3)
    graph.addEdge(2, 1, 4)

    print(graph.hasEdge(0, 1))  # true
    print(graph.hasEdge(1, 0))  # true

    for edge in graph.neighbors(2):
        print(f"{2} <-> {edge.to}, weight: {edge.weight}")
    # 2 <-> 0, weight: 3
    # 2 <-> 1, weight: 4

    graph.removeEdge(0, 1)
    print(graph.hasEdge(0, 1))  # false
    print(graph.hasEdge(1, 0))  # false

###########################################################################


"""
对于图结构来说，由起点 src 到目标节点 dest 的路径可能不止一条。我们需要一个 onPath 数组，
在进入节点时（前序位置）标记为正在访问，退出节点时（后序位置）撤销标记，这样才能遍历图中的所有路径，
从而找到 src 到 dest 的所有路径：

# 多叉树的遍历框架，寻找从根节点到目标节点的路径
path = []

def traverse(root, targetNode):
    # base case
    if root is None:
        return
    
    # 前序位置
    path.append(root)
    if root.val == targetNode.val:
        print("find path:", path)
    
    for child in root.children:
        traverse(child, targetNode)
    
    # 后序位置
    path.pop()


📢📢📢📢
为啥之前讲的遍历节点就不用撤销 visited 数组的标记，而这里要在后序位置撤销 onPath 数组的标记呢？
因为前文遍历节点的代码中，visited 数组的职责是保证每个节点只会被访问一次。
而对于图结构来说，要想遍历所有路径，可能会多次访问同一个节点，这是关键的区别。
"""
# 下面的算法代码可以遍历图的所有路径，寻找从 src 到 dest 的所有路径

# onPath 和 path 记录当前递归路径上的节点
on_path = [False] * len(graph)
path = []

def traverse(graph, src, dest):
    # base case
    if src < 0 or src >= len(graph):
        return
    if on_path[src]:
        # 防止死循环（成环）
        return
    # 前序位置
    on_path[src] = True
    path.append(src)
    if src == dest:
        print(f"find path: {path}")
    for e in graph.neighbors(src):
        traverse(graph, e.to, dest)
    # 后序位置
    path.pop()
    on_path[src] = False


"""
visited 和 onPath 主要的作用就是处理成环的情况，避免死循环。那如果题目告诉你输入的图结构不包含环，那么你就不需要考虑成环的情况了。
即明确说明了是DAG！！！！

797. 所有可能的路径 | 力扣 | LeetCode |  🟠
给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）
graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。
"""