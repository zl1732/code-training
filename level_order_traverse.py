from collections import deque

from utils import *
def levelOrderTraverse1(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    while q:
        cur = q.popleft()
        # 访问 cur 节点
        print(cur.val)

        # 把 cur 的左右子节点加入队列
        if cur.left is not None:
            q.append(cur.left)
        if cur.right is not None:
            q.append(cur.right)


def levelOrderTraverse2(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    # 记录当前遍历到的层数（根节点视为第 1 层）
    depth = 1

    while q:
        sz = len(q)
        printListofTreeNode(q)
        for i in range(sz):
            cur = q.popleft()
            # 访问 cur 节点，同时知道它所在的层数
            print(f"depth = {depth}, val = {cur.val}")

            # 把 cur 的左右子节点加入队列
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
        depth += 1


class State:
    def __init__(self, node, depth):
        self.node = node
        self.depth = depth
def levelOrderTraverse3_Original(root):
    if root is None:
        return
    q = deque()
    # 根节点的路径权重和是 1
    q.append(State(root, root.depth))

    while q:
        cur = q.popleft()
        # 访问 cur 节点，同时知道它的路径权重和
        print(f"depth = {cur.depth}, val = {cur.node.val}")

        # 把 cur 的左右子节点加入队列
        if cur.node.left is not None:
            left_depth = cur.node.left.depth
            q.append(State(cur.node.left, cur.depth + left_depth))
        if cur.node.right is not None:
            right_depth = cur.node.right.depth
            q.append(State(cur.node.right, cur.depth + right_depth))


def levelOrderTraverse3(root):
    if root is None:
        return
    q = deque()
    # 根节点的路径权重和是 1
    q.append(State(root, root.depth))

    level=1
    while q:
        sz = len(q)
        printListofTreeNode(q)
        for i in range(sz):
            cur = q.popleft()
            # 访问 cur 节点，同时知道它的路径权重和
            print(f"level={level}, val = {cur.node.val}, depth = {cur.depth}")

            # 把 cur 的左右子节点加入队列
            if cur.node.left is not None:
                left_depth = cur.node.left.depth
                q.append(State(cur.node.left, cur.depth + left_depth))
            if cur.node.right is not None:
                right_depth = cur.node.right.depth
                q.append(State(cur.node.right, cur.depth + right_depth))
        level += 1





tree = [3,9,2,1,None,5,7]
root = TreeNode().buildTree(tree)
# levelOrderTraverse2(root)

tree2 = [(3,2),(9,1),(2,3),(1,5),None,(5,2),(7,4)]
root = TreeNode().buildTreeWithDepth(tree2)
visualizeTreePretty(root)
levelOrderTraverse3(root)
