
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
