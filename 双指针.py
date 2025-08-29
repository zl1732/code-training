# 力扣 26. 删除有序数组中的重复项。
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        slow = 0 
        fast = 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                # 优化：
                # if slow != fast:
                    # nums[slow] = nums[fast]
                """
                ✅ 优化带来的好处
                    减少不必要写操作，提升性能（尤其在大数组中，避免 cache miss 或 SSD 写放大）
                    对 无重复数据 的情况有明显优化
                    在本题中不是“必须”，但是一种“精致优化”
                ✅ 实际性能影响
                    理论复杂度仍为 O(N)，但减少了 write 次数
                    在真实环境（如嵌入式或大数据）中，这种“少写”优化是很有意义的
                """
            fast += 1
        # 数组长度为索引 + 1
        return slow + 1
    
# 看看力扣第 83 题「删除排序链表中的重复元素」
# 唯一的区别是把数组赋值操作变成操作指针而已
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        slow, fast = head, head
        while fast is not None:
            if fast.val != slow.val:
                # nums[slow] = nums[fast];
                slow.next = fast
                # slow++;
                slow = slow.next
            # fast++
            fast = fast.next
        # 断开与后面重复元素的连接
        slow.next = None
        return head
    

"""
只要数组有序，就应该想到双指针技巧

* 求满足条件的子数组，一般是前缀和、滑动窗口，经常结合哈希表；
* 区间操作元素，一般是前缀和、差分数组、线段树；
* 数组有序，主要是双指针技巧，更大概率会用到二分搜索。
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 一左一右两个指针相向而行
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                # 题目要求的索引是从 1 开始的
                return [left + 1, right + 1]
            elif sum < target:
                # 让 sum 大一点
                left += 1
            elif sum > target:
                # 让 sum 小一点
                right -= 1
        return [-1, -1]
    

"""
反转数组
只要跟顺序相关的就应该想到 双指针技巧
"""
def reverseString(s: List[str]) -> None:
    # 一左一右两个指针相向而行
    left, right = 0, len(s) - 1
    while left < right:
        # 交换 s[left] 和 s[right]
        temp = s[left]
        s[left] = s[right]
        s[right] = temp    
        left += 1
        right -= 1

"""
回文串判断
"""
def isPalindrome(s: str) -> bool:
    # 一左一右两个指针相向而行
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


"""
最长回文
中间向两端扩散指针 + 递归搜索
"""
# 在 s 中寻找以 s[l] 和 s[r] 为中心的最长回文串
# 输入相同的 l 和 r，就相当于寻找长度为奇数的回文串，如果输入相邻的 l 和 r，则相当于寻找长度为偶数的回文串。
def palindrome(s: str, l: int, r: int) -> str:
    # 防止索引越界
    while l >= 0 and r < len(s) and s[l] == s[r]:
        # 双指针，向两边展开
        l -= 1
        r += 1
    # 此时 s[l+1..r-1] 就是最长回文串
    return s[l + 1: r]

# for i in range(len(s)):
#     # 奇数长度
#     palindrome(s, i, i)
#     # 偶数长度
#     palindrome(s, i, i + 1)

def longestPalindrome(self, s: str) -> str:
    res = ""
    for i in range(len(s)):
        # 以 s[i] 为中心的最长回文子串
        s1 = self.palindrome(s, i, i)
        # 以 s[i] 和 s[i+1] 为中心的最长回文子串
        s2 = self.palindrome(s, i, i + 1)
        # res = longest(res, s1, s2)
        res = res if len(res) > len(s1) else s1
        res = res if len(res) > len(s2) else s2
    return res