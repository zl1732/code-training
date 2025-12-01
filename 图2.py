# 📌 模板 A（你熟的）—— visited 判重

# 用于所有图的 DFS（无向图 / 有向图都能用）

visited = set()

def dfs(u):
    if u in visited:
        return
    visited.add(u)

    for v in graph[u]:
        dfs(v)


# 判断是否访问过

# 防止循环

# 通用性：最高




# 📌 模板 B（无向树专用）—— parent 阻断“回头边”

# 这是图论里“DFS 生成树（DFS tree）”的标准写法。

def dfs(u, parent):
    for v in graph[u]:
        if v == parent:  
            continue      # 不走回头的父节点
        dfs(v, u)


# 核心思想：

# 「无向图」每条边都有两条路径：u→v 和 v→u
# 所以通过 parent 把“回到父节点”的那一条边砍掉，就变成一棵有向树。

# 通用性：
# ✔ 无向图树
# ✔ 无向图的 DFS spanning tree
# ✔ LCA（Tarjan）
# ✔ 树上 DP
# ✔ 树中找环
# ✔ 树上路径问题
# ✔ 最小环
# ✔ 树重心
# ✔ DSG/DP on tree 系题目

# 你以后刷高级图论，全都是这种写法。