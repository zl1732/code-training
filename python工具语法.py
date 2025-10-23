from sortedcontainers import SortedList

window = SortedList()

# 添加元素
window.add(5)
window.add(1)
window.add(3)
print(window)        # SortedList([1, 3, 5])  ← 自动升序

# 按值删除
window.remove(3)
print(window)        # SortedList([1, 5])

# 按下标删除
window.pop(0)
print(window)        # SortedList([5])




"""
2️⃣ 可以直接比较 str 吗？

✅ 可以的！

在 Python 里，比较 '2' < '3' 会返回 True，
因为字符 '0'~'9' 的 ASCII 码顺序就是递增的。

'0' < '1' < '2' < '3' < ... < '9'
"""