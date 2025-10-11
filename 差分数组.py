def chafen(nums, bookings):
    n = len(nums)
    diff = [0] * (n + 1)   # 差分数组，多开一位

    # 处理所有操作
    for l, r, val in bookings:
        diff[l] += val
        diff[r + 1] -= val
    print(diff)

    # 前缀和还原数组
    res = [0] * n
    cur = 0
    for i in range(n):
        cur += diff[i]
        res[i] = nums[i] + cur
        print(i, res)
    return res
    
    # res = [0] * n
    # for i in range(n):
    #     res[i] = nums[i] + diff[i]
    #     diff[i+1] += diff[i]
    # print(res)


# 测试
nums = [1,2,3,4,5,6,7,8,9,10]
bookings = [[0,3,3],[5,7,2]]   # 区间 [0,3] +3, [5,7] +2
print(chafen1(nums, bookings))


# 差分数组工具类
class Difference:
    def __init__(self, nums: List[int]):
        if not nums:
            self.diff = []
            return
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]

    def increment(self, i: int, j: int, val: int) -> None:
        self.diff[i] += val
        if j + 1 <= len(self.diff) - 1:
            self.diff[j + 1] -= val

    def result(self) -> List[int]:
        res = [0] * len(self.diff)
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i - 1] + self.diff[i]
        return res

