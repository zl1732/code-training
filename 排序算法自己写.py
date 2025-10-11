"""
| 算法         | 时间复杂度           | 空间     | 稳定性   | 备注           |
| ----------- | ------------------ | ---------| ------- | ------------ |
| 冒泡 Bubble  | O(n²)              | O(1)     | ✅ 稳定  | 小学算法，了解即可    |
| 选择 Select  | O(n²)              | O(1)     | ❌ 不稳定 | 永远选择最小，容易跳位置 |
| 插入 Insert  | O(n²) / O(n)       | O(1)     | ✅ 稳定  | 局部有序/几乎有序时很快 |
| 希尔 Shell   | O(n^1.3 \~ n^1.6)  | O(1)     | ❌ 不稳定 | 插入排序的优化      |
| 快速 Quick   | O(n log n) / O(n²) | O(log n) | ❌ 不稳定 | 面试必会，快且原地    |
| 归并 Merge   | O(n log n)         | O(n)     | ✅ 稳定   | 面试必会，稳定但用空间  |
| 堆排 Heap    | O(n log n)         | O(1)     | ❌ 不稳定 | 建堆 + 每次取最大   |
| 桶排序 Bucket | O(n + k)\~O(n²)   | O(n + k) | ✅       | 适合均匀小数，非通用   |
| 基数排序 Radix | O(nk)             | O(n + k) | ✅      | 整数排序、定长字符串专用 |


| 会写代码 + 会讲原理         |
| ------------------- |
| ✅ 快排（重点）            |
| ✅ 归并（和快排互补）         |
| ✅ 堆排序（和 heap 结构一起学） |
| ✅ 插入排序（考细节/优化）      |"""
# 选择排序
def sort(nums: List[int]) -> None:
    n = len(nums)
    sortedIndex = 0
    while sortedIndex < n:
        minIndex = sortedIndex
        for i in range(sortedIndex + 1, n):
            if nums[i] < nums[minIndex]:
                minIndex = i
        nums[sortedIndex], nums[minIndex] = nums[minIndex], nums[sortedIndex]
        sortedIndex += 1


# 选择排序-稳定
def sort(nums):
    n = len(nums)
    sortedIndex = 0
    while sortedIndex < n:
        minIndex = sortedIndex
        for i in range(sortedIndex + 1, n):
            if nums[i] < nums[minIndex]:
                minIndex = i
        minVal = nums[minIndex]
        for i in range(minIndex, sortedIndex, -1): # 逆向
            nums[i] = nums[i - 1]
        nums[sortedIndex] = minVal
        sortedIndex += 1


# 冒泡排序法
def sort_list(nums):
    n = len(nums)
    sorted_index = 0
    while sorted_index < n:
        for i in range(n - 1, sorted_index, -1):
            if nums[i] < nums[i - 1]:
                nums[i], nums[i-1] = nums[i-1],nums[i]
                # tmp = nums[i]
                # nums[i] = nums[i - 1]
                # nums[i - 1] = tmp
        sorted_index += 1



# 冒泡-swap-earlystop  
def sort_list(nums):
    n = len(nums)
    sorted_index = 0
    while sorted_index <n:
        # 每个循环检测一次
        swap = False
        for i in range(n-1, sorted_index, -1):
            if nums[i] < nums[i - 1]:
                nums[i], nums[i-1] = nums[i-1],nums[i]
                swap = True
        if not swap:
            break
        sorted_index += 1
            
        

# 插入排序
"""
交换式（你写的）：
当前元素和前一个比较，如果小就交换；
一路交换到正确位置为止；
好处：直观，好理解。
缺点：每次移动要 3 次赋值（交换）。
"""
def sort(nums):
    n = len(nums)
    sorted_index = 0
    while sorted_index < n:
        for i in range(sorted_index, 0, -1):
            if nums[i] < nums[i - 1]:
                nums[i], nums[i-1] = nums[i-1],nums[i]
            else:
                break
        sorted_index += 1


"""
移动式（教材里的）：
先保存当前元素到 key；
把比它大的元素全部往后挪；
最后一次性插入 key。
好处：少了很多交换，赋值次数更少，效率略高。
"""

def sort(nums):
    n = len(nums)
    sorted_index = 0
    while sorted_index<n:
        cur = nums[sorted_index]
        for i in range(sorted_index, 0, -1):
            if nums[i] > cur:
                nums[i+1] = nums[i]
            # 注意如果要用移动式必须break
            else:
                break
        nums[i + 1] = cur


def insertion_sort(nums):
    n = len(nums)
    for sorted_index in range(1, n):
        cur = nums[sorted_index]
        i = sorted_index - 1
        while i >= 0 and nums[i] > cur:
            nums[i + 1] = nums[i]  # 后移
            i -= 1
        nums[i + 1] = cur



# 希尔排序 shell sort
"""先取一个步长 h，把数组分成若干个 相隔 h 的子序列。
（例如 h=3 时，下标为 0,3,6… 的元素组成一组，下标为 1,4,7… 另一组…）
在这些子序列上分别做插入排序（因为间隔大，元素“跨越式”移动，一次就能走很远）。
逐渐缩小步长（通常除以 2 或除以 3），直到步长为 1，最后做一次普通插入排序。
由于前面已经让数组“部分有序”，最后的插入排序就会非常快。"""
# 交换式
def sort(nums):
    n = len(nums)
    h =  n // 2 
    while h >= 1:
        sorted_index = h
        while sorted_index < n:
            i = sorted_index
            while i >= h:
                if nums[i] < nums[i - h]:
                    nums[i], nums[i-h] = nums[i-h],nums[i]
                else:
                    break
                i -= h
            sorted_index += 1
        h //= 2

def sort(nums):
    n = len(nums)
    h = n//2
    while h>0:
        sorted_index = h
        while sorted_index < n:
            for i in range(sorted_index, h-1, -h):
                if nums[i] < nums[i - h]:
                    nums[i], nums[i-h] = nums[i-h],nums[i]
                else:
                    break
            sorted_index += 1
        h //= 2





# 移动式
def shell_sort(nums):
    n = len(nums)
    h = n // 2  # 初始步长
    while h>0:
        for sorted_index in range(h, n):
            cur = nums[sorted_index]
            i = sorted_index-h
            while i>=h and nums[i] > cur:
                nums[i+h] = nums[i]
                i-=h
            nums[i+h]=cur
        h //= 2


def shell_sort(nums):
    n = len(nums)
    h = n // 2  # 初始步长
    while h>0:
        for sorted_index in range(h, n):
            cur = nums[sorted_index]
            i = sorted_index
            while i >= h and nums[i - h] > cur:
                nums[i] = nums[i - h]
                i -= h
            nums[i] = cur
        h //= 2
    



# 快排 前序
def sort(nums: List[int], lo: int, hi: int):
    if lo >= hi:
        return
    p = partition(nums, lo, hi)
    sort(nums, lo, p - 1)
    sort(nums, p + 1, hi)


#Lomuto1
def partition(nums, lo, hi):
    pivot = nums[hi]
    i = lo-1  # i 指向最后一个 <= pivot 元素的下标。
    for j in range(lo, hi):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]  
    nums[i+1], nums[hi] = nums[hi], nums[i+1]
    return i+1


#Lomuto2
def partition(nums, lo, hi):
    pivot = nums[hi]
    i = lo  # i 指向 pivot 的位置。
    for j in range(lo, hi):
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[hi] = nums[hi], nums[i]
    return i




# #Hoare ？？？
# def partition(nums: List[int], lo: int, hi: int) -> int:
#     pivot = nums[lo]
#     i, j = lo + 1, hi

#     while i <= j:
#         while i < hi and nums[i] <= pivot:
#             i += 1
#         while j > lo and nums[j] > pivot:
#             j -= 1
#         if i >= j:
#             break
#         nums[i], nums[j] = nums[j], nums[i]
#     nums[lo], nums[j] = nums[j], nums[lo]
#     return j



# 归并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged




# 堆排序
"""
方法	方向	                应用场景	    是否构建整棵堆	         是否递归
swim	自底向上（Bottom-Up）	插入元素时用	❌ 否，只处理一个元素	❌ 通常迭代
sink	自顶向下（Top-Down）	删除堆顶/建堆	✅ 是	               ✅ 可递归/迭代
"""
# heapify 就是sink操作, 递归写法
def heapify(nums, n, i):
    largest = i    # 先假设根节点最大
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and nums[l] > nums[largest]:
        largest = l
    if r < n and nums[r] > nums[largest]:
        largest = r
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)



# 迭代写法
def max_heap_sink(nums, n, i):
    while True:
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n and nums[l] > nums[largest]:
            largest = l
        if r < n and nums[r] > nums[largest]:
            largest = r

        if largest == i:
            break

        nums[i], nums[largest] = nums[j], nums[largest]
        i = largest




# swim操作
def max_heap_swim(nums, i):
    while i > 0 and nums[i] > nums[(i - 1) // 2]:
        nums[i], nums[parent] = nums[j], nums[(i - 1) // 2]
        i = (i - 1) // 2  # parent
    
def swim(nums, i):
    while i>0 and nums[i] > nums[parent(i)]:
        swap(i, parent(i))
        i == parent(i)



# 堆排序   
def sort(nums):
    n = len(nums)
    # 1.onlogn
    """
    每次添加一个元素 i，前面的 [0..i-1] 已经是一个合法的堆。
    所以 必须从前往后，才能保证插入元素之前，堆是有效的。
    """
    for i in range(len(nums)):
        max_heap_swim(nums, i)
    # 2.on
    for i in range(n // 2 - 1, -1, -1): # n // 2 - 1 更常用
        max_heap_sink(nums, i, n)

    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]  # 交换堆顶和末尾
        heapify(nums, i, 0)  # 调整剩余堆



# 计数排序
def sort(nums):
    min_val = min(nums)
    max_val = max(nums)
    
    offset = -min_val
    count = [0] * (max_val - min_val + 1)
    
    for num in nums:
        count[num + offset] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    sorted_nums = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        sorted_nums[count[nums[i] + offset] - 1] = nums[i]
        count[nums[i] + offset] -= 1
    
    for i in range(len(nums)):
        nums[i] = sorted_nums[i]



def counting_sort_numeric(nums):
    if not nums:
        return nums
    mn, mx = min(nums), max(nums)
    off = -mn
    count = [0] * (mx - mn + 1)

    for x in nums:
        count[x + off] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    out = [0] * len(nums)
    for x in reversed(nums):           # 倒序保证稳定
        idx = x + off
        count[idx] -= 1
        out[count[idx]] = x
    return out

