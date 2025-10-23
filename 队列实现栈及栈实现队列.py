"""
队列基本功能：
"""
class MyQueue:

    # 添加元素到队尾
    def push(self, x: int) -> None:
        pass

    # 删除队头的元素并返回
    def pop(self) -> int:
        pass

    # 返回队头元素
    def peek(self) -> int:
        pass

    # 判断队列是否为空
    def empty(self) -> bool:
        pass

"""
双栈实现队列：
    队头            队尾
    -------    -------
      s2   |  |  s1
    -------    -------
"""
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # 添加元素到队尾
    def push(self, x: int) -> None:
        self.s1.append(x)

    # 删除队头元素并返回
    def pop(self) -> int:
        # 先调用 peek 保证 s2 非空
        self.peek()
        return self.s2.pop()

    # 返回队头元素
    def peek(self) -> int:
        if not self.s2:
            # 把 s1 元素压入 s2
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    # 判断队列是否为空
    def empty(self) -> bool:
        return not self.s1 and not self.s2
    


"""
栈基本功能
"""
class MyStack:

    # 添加元素到栈顶
    def push(self, x: int) -> None:
        pass
    
    # 删除栈顶的元素并返回
    def pop(self) -> int:
        pass
    
    # 返回栈顶元素
    def top(self) -> int:
        pass
    
    # 判断栈是否为空
    def empty(self) -> bool:
        pass

        
"""用队列实现栈"""
from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()
        self.top_elem = 0

    # 将元素 x 压入栈顶
    def push(self, x: int) -> None:
        # x 是队列的队尾，是栈的栈顶
        self.q.append(x)
        self.top_elem = x

    # 返回栈顶元素
    def top(self) -> int:
        return self.top_elem

    # 删除栈顶的元素并返回
    def pop(self) -> int:
        size = len(self.q)
        # 留下队尾 2 个元素
        while size > 2:
            self.q.append(self.q.popleft())
            size -= 1
        # 记录新的队尾元素
        self.top_elem = self.q[0]
        self.q.append(self.q.popleft())
        # 删除之前的队尾元素
        return self.q.popleft()

    # 判断栈是否为空
    def empty(self) -> bool:
        return not self.q