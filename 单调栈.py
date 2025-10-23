# | 写法方向          | 栈内容        | 原因                           | 是否需要索引 | 更新逻辑             |
# | -----------     | ---------     | -----------------             | ------     | -----------        |
# | **正序（左→右）** | 索引           | 要更新左边的元素结果，需要精确定位  | ✅ 必须    | 弹出被击败者，回填结果 |
# | **倒序（右→左）** | 数值（或索引都行）| 当前元素直接从右边找更大，不需回填 | ❌ 可选    | 自己看栈顶并更新       | 


# 🧩 一、下一个更大元素（右 → 更大）
# ✅ 正序（推荐）
def next_greater(nums):
    n = len(nums)
    res = [-1] * n
    st = []  # 存索引，保持递减（栈顶最小）

    for i in range(n):
        cur = nums[i]
        while st and cur > nums[st[-1]]:
            idx = st.pop()
            res[idx] = cur
        st.append(i)
    return res


# | 关键点        | 含义                              |
# | ---------    | ------------------------------- |
# | **栈存的内容** | **还没找到更大值的索引（index）**           |
# | **栈内单调性** | 对应的 nums[st] 值单调递减（从底到顶越来越小）    |
# | **逻辑语义**   | “我向右走，每遇到更大的数，就帮左边还没找到更大值的人更新。” |
# | **时空感知**   | 栈里是“**等待被击败**”的人；新来的数是“打手”。     |
# | **更新时机**   | 弹栈时更新：`res[被弹出索引] = 当前更大数`      |

# 🧠 心理模型：
# 我一路往右走，背后的人都在等比他们更高的；
# 一旦我更高，就顺手告诉他们“我就是你们右边的更大值”。


# ✅ 倒序（直观）
# 存数字
def next_greater_rev(nums):
    n = len(nums)
    res = [-1] * n
    st = []
    for i in range(n-1, -1, -1):
        cur = nums[i]
        # 下一个更大元素
        while st and cur >= st[-1]:
        # 下一个>=元素
        #while st and cur >= st[-1]:
            st.pop()
        res[i] = -1 if not st else st[-1]
        st.append(nums[i])
    return res
# 存index
def next_greater_rev(nums):
    n = len(nums)
    res = [-1] * n
    st = []
    for i in range(n-1, -1, -1):
        cur = nums[i]
        while st and cur >= nums[st[-1]]:
            st.pop()
        res[i] = -1 if not st else nums[st[-1]]
        st.append(i)
    return res


"""
| 关键点        | 含义                              |
| ---------    | ------------------------------- |
| **栈存的内容** | **已经扫描过的、在右侧、可能是“右边更大值”的数值**    |
| **栈内单调性** | 值单调递减（栈顶最小）                     |
| **逻辑语义**   | “我往右看，清理掉那些比我矮的；栈顶就是我右边第一个更大的。” |
| **时空感知**   | 栈里是“**已经看过的右边候选人**”；我自己决定谁能留下。  |
| **更新时机**   | 每次处理当前 i 时立刻确定 `res[i]` 。       |

🧠 心理模型：
我从右往左扫描，手里拿着一叠“右边的高个子”；
比我矮的都丢掉，第一个留在栈顶的，就是我能看到的最近高个。
"""


# 🧩 二、下一个更小元素（右 → 更小）
# ✅ 正序
def next_smaller(nums):
    n = len(nums)
    res = [-1] * n
    st = []  # 存索引，保持递增（栈顶最大）

    for i in range(n):
        cur = nums[i]
        while st and cur < nums[st[-1]]:
            prev = st.pop()
            res[prev] = cur
        st.append(i)
    return res
            

# ✅ 倒序
def next_smaller_rev(nums):
    n = len(nums)
    res = [-1] * n
    st = []  # 存数值，递增
    for i in range(n-1, -1, -1):
        while st and st[-1] >= nums[i]:
            st.pop()
        res[i] = -1 if not st else st[-1]
        st.append(nums[i])
    return res



# 🧩 三、上一个更大元素（左 → 更大）

def prev_greater(nums):
    n = len(nums)
    res = [-1] * n
    st = []  # 存索引，递减栈
    # 倒序 可以存两种
    for i in range(n):
        cur = nums[i]
        while st and cur >= st[-1]:
            st.pop()
        res[i] = -1 if not st else st[-1]
        st.append(cur)
    # 正序，只能存idx
    for i in range(n-1, -1, -1):
        cur = nums[i]
        while st and cur > nums[st[-1]]:
            idx = st.pop()
            res[idx] = cur
        st.append(i)
    return res



# 🧩 四、上一个更小元素（左 → 更小）
# ✅ 正序
def prev_smaller(nums):
    n = len(nums)
    res = [-1] * n
    st = []  # 存索引，递增栈
    for i in range(n):
        while st and nums[i] <= nums[st[-1]]:
            st.pop()
        res[i] = -1 if not st else nums[st[-1]]
        st.append(i)
    return res
# ✅ 倒序
def prev_smaller_rev(nums):
    n = len(nums)
    res = [-1] * n
    st = []  # 存索引，保持单调递增

    for i in range(n-1, -1, -1):
        while st and nums[i] < nums[st[-1]]:
            idx = st.pop()
            res[idx] = nums[i]  # 我是 idx 左边第一个更小
        st.append(i)
    return res

"""
目标：找每个元素右边第一个更大的数。

| 数组形态                          | 最适合的写法 | 栈表现            | 直觉               |
| -----------------------------    | ------    | -----------      | ---------------- |
| **递减到递增** (如 `[5,4,3,2,1,6]`)| 倒序写法   | 栈短、均匀清理      | 每步都能看到右边更大       |
| **递增到递减** (如 `[6,1,2,3,4,5]`)| 正序写法   | 栈短、实时更新      | 每步都能帮左边更小的更新     |
| **乱序数组**                      | 两者差不多  | 局部堆积 + 局部清理 | 平均栈长度 O(1~log n) |
"""




def next_greater_debug_visual(nums):
    n = len(nums)
    res = [-1] * n
    st = []  # 存索引，保持递减（栈顶最小）

    def draw_stack(stack):
        """打印栈内容的可视化小图"""
        if not stack:
            print("  [栈为空]")
            return
        # 找最大高度用于缩放
        maxh = max(nums[i] for i in stack)
        print("  栈结构：")
        for h in range(maxh, 0, -1):
            line = ""
            for i in stack:
                line += "  █ " if nums[i] >= h else "    "
            print(line)
        print(" ", " ".join(f"{nums[i]:2d}" for i in stack))
        # print("  ↑↑ 栈底 → 栈顶 ↑↑")

    print(f"\nnums = {nums}")
    print("初始状态: res =", res)
    print("=" * 60)

    for i in range(n):
        print(nums)
        print(f"🔹 当前元素: i={i}, nums[i]={nums[i]}")
        while st and nums[i] > nums[st[-1]]:
            idx = st.pop()
            res[idx] = nums[i]
            print(f"  ⚙️ nums[{i}]={nums[i]} > nums[st[-1]]={nums[idx]} → 弹出 idx={idx}, res[{idx}]={nums[i]}")
            draw_stack(st)
            print("-" * 40)
        st.append(i)
        print(f"  ➕ 入栈 i={i}, 当前栈索引={st}")
        draw_stack(st)
        print(f"  📊 当前 res = {res}")
        print("=" * 60)
        print()

    print(f"✅ 最终结果: {res}\n")
    return res



# # 1️⃣ 基本例子：常规混合序列
# next_greater_debug_visual([2, 1, 2, 4, 3])

# 2️⃣ 全递减序列：最坏情况（所有元素都入栈）
next_greater_debug_visual([9, 8, 7, 6, 5])

# 3️⃣ 全递增序列：最顺畅情况（每次都立刻弹栈）
next_greater_debug_visual([1, 2, 3, 4, 5])

# # 4️⃣ 波浪序列：多次触发 while
# next_greater_debug_visual([2, 5, 1, 3, 4])

# # 5️⃣ 极端情况：全相等
# next_greater_debug_visual([3, 3, 3, 3])



def next_greater_debug_clean(nums):
    n = len(nums)
    res = [-1] * n
    st = []  # 存索引

    print(f"\nnums = {nums}")
    print("=" * 50)
    for i in range(n):
        # 打印当前数组并标出当前处理元素
        print(f"\n🔹 Step {i}: 处理 nums[{i}] = {nums[i]}")
        print("   " + "  ".join(f"{x:2d}" for x in nums))
        print("    " + "    " * i + "↑")
        print()

        # while 弹栈过程
        print(f"  📦 当前索引: {st}")
        while st and nums[i] > nums[st[-1]]:
            idx = st.pop()
            res[idx] = nums[i]
            print(f"  ⚙️  {nums[i]} > nums[{idx}]={nums[idx]} → 弹出 {idx}, res[{idx}]={nums[i]}, 栈值: {[nums[x] for x in st]}")

        # 入栈
        print()
        st.append(i)
        print(f"  ➕ 入栈 {i} (值={nums[i]})")
        print(f"  📦 当前索引: {st}")
        # print(f"  📦 当前栈值: {[nums[x] for x in st]}")
        print(f"  📊 当前结果: {res}")
        print()

        print("-" * 50)
        

    print(f"✅ 最终结果: {res}\n")
    return res

next_greater_debug_clean([2, 1, 2, 4, 3])
# next_greater_debug_clean([5, 4, 3, 2, 1, 6])
# next_greater_debug_clean([1, 2, 3, 4, 5])

a = [1,2,3]
a.sort()
print(a)



"""
关于维护栈的单调性怎么记忆 < >号


🧠 1️⃣ 单调栈的本质

每来一个数，我就看它是否“破坏了”栈的单调性。
如果破坏了，就弹出栈顶，直到恢复单调。

口诀：谁坏我就踢谁。
“坏” = 破坏单调性。
递增栈怕小的，递减栈怕大的。

🔼 单调递增栈-严格
while st and cur <= st[-1]:
    st.pop()
[1 3 7] 5

🔼 单调递增栈-可等 
while st and cur < st[-1]:
    st.pop()
[1 3 5] 5

🔽 单调递减栈 - 严格
while st and cur >= st[-1]:
    st.pop()
[7 5 1] 3

🔽 单调递减栈 - 可等
while st and cur > st[-1]:
    st.pop()
[7 5 3] 3
"""