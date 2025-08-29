
class Node:
    def __init__(self, val: int):
        self.val = val
        self.children = []

def build_tree_from_list(data: list, root_val: int) -> Node:
    node_map = {}

    # 第一次遍历：创建所有节点
    for val, _ in data:
        if val not in node_map:
            node_map[val] = Node(val)

    # 第二次遍历：填充子节点
    for val, children_vals in data:
        node = node_map[val]
        for child_val in children_vals:
            if child_val not in node_map:
                node_map[child_val] = Node(child_val)
            node.children.append(node_map[child_val])

    return node_map[root_val]

# 打印函数
def print_tree(node, level=0):
    print(' ' * level * 2 + f'Node({node.val}), Depth({depth_dict[node.val]})')
    for child in node.children:
        print_tree(child, level + 1)

# 打印函数
def print_tree2(node, level=0, depth=0):
    print(' ' * level * 2 + f'Node({node.val}), Depth({depth})')
    for child in node.children:
        cur_depth = depth_dict[child.val]
        print_tree2(child, level + 1, depth + cur_depth)



def pre_order_traverse(root):
    if root is None:
        return

    # 访问根节点
    print(root.val)

    # 递归访问所有子节点
    for child in root.children:
        pre_order_traverse(child)
        
def post_order_traverse(root):
    if root is None:
        return
    # 递归访问所有子节点
    for child in root.children:
        post_order_traverse(child)
    # 访问根节点
    print(root.val)


from collections import deque

def level_order_traverse1(root):
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


# 变种dfs+stack
def level_order_traverse1(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    while q:
        cur = q.pop()
        # 访问 cur 节点
        print(cur.val)
        
        # 把 cur 的所有子节点加入队列
        for child in cur.children:
            q.append(child)


def level_order_travers2(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    depth=0
    while q:
        sz = len(q)
        print([node.val for node in q])
        for i in range(sz):
            # 这个不能用pop，range之后乱了
            node = q.popleft()
            print(f"depth:{depth}, node:{node.val}")
            for child in node.children:
                q.append(child)
        depth += 1


class State:
    def __init__(self, node, depth):
        self.node = node
        self.depth = depth

def level_order_traverse3(root):
    if root is None:
        return
    q = deque()
    # 记录当前遍历到的层数
    q.append(State(root,0))

    while q:
        state = q.popleft()
        cur = state.node,
        depth = state.depth
        # 访问 cur 节点，同时知道它所在的层数
        print(f"depth = {depth}, val = {cur.val}")

        for child in cur.children:
            q.append(State(child, depth + depth_dict[child.val]))
            # q.append(State(child, depth + 1))


# 示例数据和使用
data = [
    [1, [2, 3, 4]],
    [2, [5, 6]],
    [3, [7]],
    [4, []],
    [5, []],
    [6, []],
    [7, [8]],
    [8,[]]
]

depth_dict = {
    1: 0,
    2: 1,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 2,
    8: 1
}

root = build_tree_from_list(data, root_val=1)
print_tree(root)
level_order_travers2(root)
