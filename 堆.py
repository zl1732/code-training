
"""
完全二叉树是关键

想要用数组模拟二叉树，前提是这个二叉树必须是完全二叉树。
"""

def heapSort(arr):
    n = len(arr)
    
    # 1️⃣ 原地建大顶堆：从最后一个非叶子节点开始下沉
    for i in reversed(range(n // 2)):
        siftDown(arr, i, n)
        print(arr)

    # 2️⃣ 每次把堆顶最大值换到末尾，缩小堆，然后下沉调整
    for end in reversed(range(1, n)):
        arr[0], arr[end] = arr[end], arr[0]  # 最大值交换到最后
        siftDown(arr, 0, end)               # 只调整前 end 个元素
        print(arr)

def siftDown(arr, i, n):
    # arr[i] 是当前节点，n 是堆的有效长度
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # 比较左右孩子是否更大
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest == i:
            break  # 当前节点就是最大，不用动
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest  # 继续往下沉


# def heap_sort_min_heap_inplace(arr):
#     n = len(arr)

#     # 建小顶堆
#     for i in reversed(range(n // 2)):
#         sift_down(arr, i, n)
#         print(arr)

#     # 逐个取出最小值，放到后面，类似于选择排序
#     for end in reversed(range(1, n)):
#         arr[0], arr[end] = arr[end], arr[0]  # 把最小值换到末尾
#         sift_down(arr, 0, end)               # 对剩下的 [0, end) 调整小顶堆
#         print(arr)

#     # 因为是小顶堆，最后得到的是**降序**，需要反转
#     arr.reverse()

# def sift_down(arr, i, n):
#     while True:
#         smallest = i
#         l = 2 * i + 1
#         r = 2 * i + 2
#         if l < n and arr[l] < arr[smallest]:
#             smallest = l
#         if r < n and arr[r] < arr[smallest]:
#             smallest = r
#         if smallest == i:
#             break
#         arr[i], arr[smallest] = arr[smallest], arr[i]
#         i = smallest


# 上浮
def siftUp(arr, i):
    while i > 0:
        parent = (i - 1) // 2
        if arr[i] < arr[parent]:
            print(arr)
            arr[i], arr[parent] = arr[parent], arr[i]
            i = parent  # 更新当前位置，继续向上浮动
        else:
            break

def heapPush(heap, val):
    heap.append(val)              # 加到最后
    siftUp(heap, len(heap) - 1)   # 上浮调整



arr=[43,15,4,7,12,9,44]
heapSort(arr)
# heap_sort_min_heap_inplace(arr)


heapPush(arr, 1)
print(arr)



class SimpleMinPQ:
    def __init__(self, capacity):
        self.capacity = capacity
        self.heap = [0] * capacity  # 固定大小的数组
        self.size = 0               # 当前堆中元素个数

    # 父节点索引
    def parent(self, index):
        return (index - 1) // 2

    # 左右子节点索引
    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    # 交换两个索引处的值
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # 查看堆顶元素（最小值），O(1)
    def peek(self):
        if self.size == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]

    # 插入元素，O(logN)
    def push(self, value):
        if self.size >= self.capacity:
            raise OverflowError("Heap is full")
        self.heap[self.size] = value
        self._swim(self.size)
        self.size += 1

    # 弹出堆顶元素，O(logN)
    def pop(self):
        if self.size == 0:
            raise IndexError("Heap is empty")
        min_value = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self._sink(0)
        return min_value

    # 上浮调整
    def _swim(self, index):
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

        
    # 下沉调整
    def _sink(self, index):
        while True:
            smallest = index
            left = self.left(index)
            right = self.right(index)

            if left < self.size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < self.size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.swap(index, smallest)
            index = smallest

    # 打印堆内容
    def __str__(self):
        return str(self.heap[:self.size])


# 示例使用
if __name__ == "__main__":
    pq = SimpleMinPQ(5)
    for num in [3, 2, 1, 5, 4]:
        pq.push(num)

    while pq.size > 0:
        print(pq.pop())




"""

| 类型      | 项目                          | 描述                      |
| ------- | --------------------------- | ----------------------- |
| ✅ 新增    | `__len__` 方法                | 可使用 `len(pq)` 获取队列大小    |
| ❗ 健壮性   | 错误信息更明确                     | `peek` 和 `pop` 的异常提示更友好 |
| 🔁 重命名  | `_swim`, `_sink`, `_resize` | 加 `_` 表示内部私有方法，更专业      |
| 🔁 安全性  | push 时判断 `>=` 而非 `==`       | 防止 rare edge case       |
| 🔁 安全性  | `pop` 后清空引用                 | 减少内存泄漏风险（尤其对象较大时）       |
| 🔁 可维护性 | 默认初始容量改为 8                  | 避免过小容量频繁扩容              |
| 🔁 结构优化 | 缩容判断写法更稳健                   | 确保不缩到 0 大小等边界情况         |

"""

class MyPriorityQueue:
    def __init__(self, capacity=8, comparator=None):  # 🔁【改进】默认初始容量改为8，容错更强
        self.heap = [None] * capacity
        self.size = 0
        self.comparator = comparator or (lambda x, y: (x > y) - (x < y))

    def is_empty(self):
        return self.size == 0

    def __len__(self):  # ✅【新增】支持 len(pq) 获取队列大小
        return self.size

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek from an empty priority queue.")  # ❗【健壮性】错误提示更清晰
        return self.heap[0]

    def push(self, value):
        if self.size >= len(self.heap):  # 🔁【改进】原版是 self.size == len(...)，这里更稳妥
            self._resize(len(self.heap) * 2)

        self.heap[self.size] = value
        self._swim(self.size)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty priority queue.")  # ❗【健壮性】

        min_value = self.heap[0]
        self.swap(0, self.size - 1)
        self.heap[self.size - 1] = None  # 🔁【改进】清除引用，防内存泄漏
        self.size -= 1
        self._sink(0)

        if 0 < self.size <= len(self.heap) // 4:  # 🔁【改进】缩容判断更健壮
            self._resize(len(self.heap) // 2)

        return min_value

    def _swim(self, index):  # 🔁【重命名】swim → _swim，表示私有方法
        while index > 0 and self.comparator(self.heap[self.parent(index)], self.heap[index]) > 0:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def _sink(self, index):  # 🔁【重命名】sink → _sink
        while self.left(index) < self.size:
            smallest = index
            left = self.left(index)
            right = self.right(index)

            if left < self.size and self.comparator(self.heap[left], self.heap[smallest]) < 0:
                smallest = left
            if right < self.size and self.comparator(self.heap[right], self.heap[smallest]) < 0:
                smallest = right

            if smallest == index:
                break

            self.swap(index, smallest)
            index = smallest

    def _resize(self, capacity):  # 🔁【重命名】resize → _resize
        print(f"Resizing heap from {len(self.heap)} to {capacity}")
        new_heap = [None] * capacity
        for i in range(self.size):
            new_heap[i] = self.heap[i]
        self.heap = new_heap


# 初始 4 个元素
pq = MyPriorityQueue(2)
for num in [5, 3, 8, 1, 0]:
    pq.push(num)

# 此时堆大小 = 4，容量 = 4（扩容过）

while not pq.is_empty():
    pq.pop()
