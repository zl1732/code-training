class SegmentTree:
    def __init__(self, nums, merge_func):
        # 构造函数：初始化线段树结构
        pass

    def query(self, i, j):
        # 查询闭区间 [i, j] 上的聚合值（如最小值、最大值、和等）
        pass

    def update(self, i, val):
        # 把 nums[i] 改为 val，同时更新线段树结构
        pass

"""
🧠 解读 1：线段树 vs suffixMin
| 功能     | suffixMin 数组          | 线段树（SegmentTree） |
| -------- | -----------------------| ---------------- |
| 查询方式  | 只能查 `[i..]` 后缀最小值 | 查任意 `[i,j]` 区间   |
| 查询复杂度 | `O(1)`                | `O(log n)`       |
| 更新复杂度 | `O(n)`（要重建全部）     | `O(log n)`       |
| 灵活性    | 只能预处理一个功能（最小值）| 支持任意聚合（和、最大值等）   |


merge 函数 决定了这个“合并”的逻辑是：
    min：支持区间最小值
    max：支持区间最大值
    sum：支持区间求和
    lambda a, b: a * b：支持区间乘积
这相当于给线段树装了一个“可插拔的功能模块”。
"""

class SegmentTree:
    def __init__(self, nums, merge):
        """
        构造函数，构建线段树
        :param nums: 原始数组
        :param merge: 一个二元函数，比如 min/max/sum，用于控制 query 的逻辑
        """
        self.n = len(nums)
        self.merge = merge              # 合并函数，比如 min/max/sum
        self.tree = [0] * (4 * self.n)  # 分配足够空间构建线段树
        self._build(nums, 0, 0, self.n - 1)

    def _build(self, nums, idx, l, r):
        """
        递归构建线段树，idx 表示当前节点在 tree 数组中的索引
        l, r 表示当前节点管理的区间范围 [l, r]
        """
        if l == r:
            self.tree[idx] = nums[l]
            return
        mid = (l + r) // 2
        self._build(nums, idx*2+1, l, mid)         # 构建左子树
        self._build(nums, idx*2+2, mid+1, r)       # 构建右子树
        self.tree[idx] = self.merge(self.tree[idx*2+1], self.tree[idx*2+2])  # 合并子节点结果

    def query(self, ql, qr):
        """
        查询闭区间 [ql, qr] 的合并值（最小值、最大值、和等）
        """
        return self._query(0, 0, self.n - 1, ql, qr)

    def _query(self, idx, l, r, ql, qr):
        """
        递归查询
        idx：当前节点索引
        l, r：当前节点代表的区间
        ql, qr：要查询的目标区间
        """
        if qr < l or r < ql:
            # 查询区间与当前节点无交集
            return self._default_value()
        if ql <= l and r <= qr:
            # 当前节点完全被包含在查询区间中
            return self.tree[idx]
        mid = (l + r) // 2
        left = self._query(idx*2+1, l, mid, ql, qr)
        right = self._query(idx*2+2, mid+1, r, ql, qr)
        return self.merge(left, right)

    def update(self, i, val):
        """
        更新 nums[i] = val，同时维护线段树
        """
        self._update(0, 0, self.n - 1, i, val)

    def _update(self, idx, l, r, i, val):
        if l == r:
            self.tree[idx] = val
            return
        mid = (l + r) // 2
        if i <= mid:
            self._update(idx*2+1, l, mid, i, val)
        else:
            self._update(idx*2+2, mid+1, r, i, val)
        self.tree[idx] = self.merge(self.tree[idx*2+1], self.tree[idx*2+2])

    def _default_value(self):
        """
        返回 merge 操作的单位元（identity element）
        比如 min 用 inf，max 用 -inf，sum 用 0
        """
        if self.merge == min:
            return float('inf')
        elif self.merge == max:
            return float('-inf')
        elif self.merge == sum:
            return 0
        else:
            raise NotImplementedError("请自定义 merge 时，重写 _default_value")


nums = [3, 1, 4, 2]

# 最小值线段树
min_tree = SegmentTree(nums, merge=min)
print("min(1..3) =", min_tree.query(1, 3))  # 输出 1
min_tree.update(2, 0)
print("min(1..3) =", min_tree.query(1, 3))  # 输出 0

# 最大值线段树
max_tree = SegmentTree(nums, merge=max)
print("max(0..2) =", max_tree.query(0, 2))  # 输出 4
max_tree.update(1, 5)
print("max(0..2) =", max_tree.query(0, 2))  # 输出 5

# 区间和线段树（用 sum 本身作为 merge 会出错，需 lambda）
sum_tree = SegmentTree(nums, merge=lambda a, b: a + b)
print("sum(1..3) =", sum_tree.query(1, 3))  # 输出 6
sum_tree.update(3, 10)
print("sum(1..3) =", sum_tree.query(1, 3))  # 输出 14
