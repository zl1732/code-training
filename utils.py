

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

class TreeNode:
    def __init__(self, val=0, depth=0, left=None, right=None):
        self.val = val
        self.depth = depth
        self.left = left
        self.right = right
        
    def buildTree(self, values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        for i in range(len(nodes)):
            if nodes[i] is not None:
                if 2 * i + 1 < len(nodes):
                    nodes[i].left = nodes[2 * i + 1]
                if 2 * i + 2 < len(nodes):
                    nodes[i].right = nodes[2 * i + 2]
        return nodes[0]
    
    def buildTreeWithDepth(self, values_depths):
        if not values_depths:
            return None
        nodes = [TreeNode(vp[0],vp[1]) if vp is not None else None for vp in values_depths]
        for i in range(len(nodes)):
            if nodes[i] is not None:
                if 2 * i + 1 < len(nodes):
                    nodes[i].left = nodes[2 * i + 1]
                if 2 * i + 2 < len(nodes):
                    nodes[i].right = nodes[2 * i + 2]
        return nodes[0]
    
def visualizeTreePretty(root):
    from anytree import Node, RenderTree
    if root is None:
        print("Tree is empty")
        return
    
    def buildAnyTree(parent, node):
        if node is None:
            return None
        # 先显示 val 再显示 depth
        if parent:
            node_name = f"{node.val} (depth={node.depth})"
        else:
            node_name = f"{node.val} (depth={node.depth})"
        any_node = Node(node_name, parent=parent)
        buildAnyTree(any_node, node.left)
        buildAnyTree(any_node, node.right)
        return any_node
    
    any_root = buildAnyTree(None, root)
    for pre, fill, node in RenderTree(any_root):
        print(f"{pre}{node.name}")

def printListofTreeNode(nodes):
    for node in nodes:
        if isinstance(node, TreeNode):
            print(node.val, end=' ')
        elif isinstance(node, State):
            print(node.node.val, end=' ')
        else:
            print('None', end=' ')
    print()

