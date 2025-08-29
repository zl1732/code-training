from typing import List

# 多叉树节点
class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []

# 多叉树的遍历
def traverse(root):
    if root is None:
        return
    print(f"visit {root.val}")  # 前序位置
    for child in root.children:
        traverse(child)
    # 后序位置（可选）

# 图节点
class Vertex:
    def __init__(self, id=0, neighbors=None):
        self.id = id
        self.neighbors = neighbors if neighbors is not None else []

# 图的遍历
def traverse_graph(s: Vertex, visited: List[bool]):
    if s is None or visited[s.id]:
        return
    visited[s.id] = True
    print(f"visit {s.id}")  # 前序位置
    for neighbor in s.neighbors:
        traverse_graph(neighbor, visited)
    # 后序位置（可选）

# ========== 测试用例 ==========

# 1. 测试多叉树遍历
print("多叉树遍历:")
# 构造如下多叉树:
#         1
#      /  |  \
#     2   3   4
#        / \
#       5   6
tree = Node(1, [
    Node(2),
    Node(3, [Node(5), Node(6)]),
    Node(4)
])
traverse(tree)

# 2. 测试图遍历
print("\n图遍历:")
# 构造如下图:
#     0 —— 1
#     |    |
#     3 —— 2
# 环：0-1-2-3-0
v0 = Vertex(0)
v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)

v0.neighbors = [v1, v3]
v1.neighbors = [v0, v2]
v2.neighbors = [v1, v3]
v3.neighbors = [v0, v2]

# 顶点数为4，visited 初始化为 False
visited = [False] * 4
traverse_graph(v0, visited)
