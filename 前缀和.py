class NumMatrix:
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        self.preSum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 计算每个矩阵 [0, 0, i, j] 的元素和
                self.preSum[i][j] = (self.preSum[i - 1][j] + self.preSum[i][j - 1] +
                                     matrix[i - 1][j - 1] - self.preSum[i - 1][j - 1])
                # self.preSum[i][j] = self.preSum[i-1][j] + self.preSum[i][j-1] - \
                #                     self.preSum[i-1][j-1] + matrix[i-1][j-1]                

    def sumRegion(self, x1, y1, x2, y2):
        # 目标矩阵之和由四个相邻矩阵运算获得
        # 注意x1, y1要包含，所以是x1-1,y1-1的部分去除
        return (self.preSum[x2 + 1][y2 + 1] - self.preSum[x1][y2 + 1] -
                self.preSum[x2 + 1][y1] + self.preSum[x1][y1])
    





# [560] 和为 K 的子数组
def subarraySum1(nums, k):
    count = {0: 1}  # 前缀和为0出现1次（空数组前缀）
    preSum = 0
    out = 0
    for num in nums:
        print(num)
        preSum += num
        if preSum - k in count:
            out += count[preSum - k]
        print(count)
        """注意每次都更新"""
        count[preSum] = count.get(preSum, 0) + 1
        print(count)
    return out

from collections import defaultdict
def subarraySum( nums, k):
    count = defaultdict(list)
    count[0].append(-1)  # 前缀和=0 出现过下标 -1
    preSum = 0
    out = 0
    for i, num in enumerate(nums):
        print(i)
        preSum += num
        if preSum-k in count:
            out += len(count[preSum-k])
        """应该放在后面"""
        print(count)

        count[preSum].append(i)
        print(count)

    return out

nums = [1,-2,1,2,-1,2,3]
k = 3
# subarraySum(nums, k)


print(-1%4)
print(-2%4)