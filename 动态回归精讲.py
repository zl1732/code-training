"""
求解动态规划的核心问题是穷举
动态规划问题的一般形式就是求最值
    比如说让你求最长递增子序列呀，最小编辑距离。


重叠子问题、最优子结构、状态转移方程就是动态规划三要素:
    1. 只有列出正确的「状态转移方程」，才能正确地穷举。
    2. 需要判断算法问题是否具备「最优子结构」
    3. 动态规划问题存在「重叠子问题」，需要你使用「备忘录」或者「DP table」来优化穷举过程

思维框架，辅助你思考状态转移方程：
    明确「状态」-> 明确「选择」 -> 定义 dp 数组/函数的含义。
"""

"""
🧠 一、动态规划的本质是什么？
    把问题拆成子问题；
    用「状态转移方程」描述子问题之间的关系；
    利用「备忘录或DP表」来缓存已经算过的子问题，避免重复计算。

| 名称       | 意思                    | 通俗解释                                                             |
| --------   | ----------------      | ---------------------------------------------------------------- |
| ✅ 状态     | 描述当前子问题的参数      | 比如“背包还有多大空间、你走到了第几个物品”                                           |
| ✅ 选择     | 当前可以做的决策         | 比如“装还是不装这个物品”，“往右还是往下走”                                          |
| ✅ 状态转移方程| 用子问题的解来推原问题的解的公式 | 比如 `dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])` |

"""


"""
🔥🔥🔥 《递归》  《迭代》
第一种是带备忘录的递归解法，或称为「自顶向下」的解法，也就是我们上面展示的，一个递归函数带一个 memo 备忘录。

第二种是 DP table 的迭代解法，或称为「自底向上」的解法，也就是你说的，用 for 循环去迭代 dp 数组进行求解。

这两者的本质是一样的，可以互相转化。迭代解法中的那个 dp 数组，就是递归解法中的 memo 数组。

"""


"框架1"
# 自顶向下递归的动态规划
def dp(状态1, 状态2, ...):
    if 状态已经计算过:
        return 记忆值
    for 选择 in 所有选择:
        # 根据选择更新状态
        result = 求最值(result, dp(新状态1, 新状态2, ...))
    保存结果
    return result


"""
1. 《递归》解法（从上到下）
注意他这个写法，依然类似用一个traverse+全局变量
由于本算法不存在冗余计算，子问题个数为 O(n)
"""
def fib(n: int) -> int:
    # 备忘录全初始化为 -1
    # 因为斐波那契数肯定是非负整数，所以初始化为特殊值 -1 表示未计算

    # 因为数组的索引从 0 开始，所以需要 n + 1 个空间
    # 这样才能把 `f(0) ~ f(n)` 都记录到 memo 中
    memo = [-1] * (n + 1)

    return self.dp(memo, n)

# 带着备忘录进行递归
def dp(memo: list, n: int) -> int:
    # base case
    if n == 0 or n == 1:
        return n
    # 已经计算过，不用再计算了
    if memo[n] != -1:
        return memo[n]
    # 在返回结果之前，存入备忘录
    memo[n] = self.dp(memo, n - 1) + self.dp(memo, n - 2)
    return memo[n]


"框架2"
# 自底向上迭代的动态规划
# 初始化 base case
dp[初始状态] = 初始值
# 逐步填表
for 状态1 in 状态1所有取值:
    for 状态2 in 状态2所有取值:
        for 每个选择:
            dp[当前状态] = 求最值(由上一个状态+选择得到的值)


"""
2. 《迭代》解法（从下到上）
"""
def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    # dp table
    dp = [0] * (n + 1)
    # base case
    dp[0] = 0
    dp[1] = 1
    # 状态转移
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


"""
| 抽象框架                   | 实际写法                        |
| --------------------      | --------------------------- |
| `dp[0] = base case`       | `dp[0] = 0`                 |
| `dp[1] = base case`       | `dp[1] = 1`                 |
| `for 状态 in 状态的所有取值:`| `for i in range(2, n+1):`   |
| `dp[i] = 求最值(...)`      | `dp[i] = dp[i-1] + dp[i-2]` |

"""

# 你有 n 个物品和一个容量为 W 的背包，每个物品有重量 w[i] 和价值 v[i]。每个物品只能选一次，求最大价值。
n = len(weight)
W = 背包容量
dp = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(0, W + 1):
        if weight[i - 1] > w:
            dp[i][w] = dp[i - 1][w]  # 装不下，不能选
        else:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight[i - 1]] + value[i - 1])

"""
| 抽象伪代码部分                   | 实际代码中的内容                                |
| ---------------------------    | --------------------------------------- |
| `dp[0][0][...] = base case`    | `dp[0][...] = 0` 表示什么都不选，价值为 0          |
| `for 状态1 in 状态1的所有取值:`   | `for i in range(1, n+1):`  —— 状态1是物品数   |
| `for 状态2 in 状态2的所有取值:`   | `for w in range(0, W+1):` —— 状态2是当前背包容量 |
| `dp[...] = 求最值(...)`         | `dp[i][w] = max(...)` —— 选 or 不选        |

"""





"""
这里引出了“状态转移方程”这个名词，实际上就是描述问题结构的数学形式。
状态转移方程如下：

    f(n) = {
              0               , n = 0
              1               , n = 1
              f(n-1) + f(n-2) , n > 1
           }
这个方程表示斐波那契数列的定义方式，其中每一项的值由前两项相加得到。


细心的读者会发现，根据斐波那契数列的状态转移方程，当前状态 n 只和之前的 n-1, n-2 两个状态有关，
其实并不需要那么长的一个 DP table 来存储所有的状态，只要想办法存储之前的两个状态就行了。
所以，可以进一步优化，把空间复杂度降为 O(1)

这一般是动态规划问题的最后一步优化，如果我们发现每次状态转移只需要 DP table 中的一部分，
那么可以尝试缩小 DP table 的大小，只记录必要的数据，从而降低空间复杂度。
"""
def fib(n: int) -> int:
    if n == 0 or n == 1:
        # base case
        return n
    # 分别代表 dp[i - 1] 和 dp[i - 2]
    dp_i_1, dp_i_2 = 1, 0
    for i in range(2, n + 1):
        # dp[i] = dp[i - 1] + dp[i - 2];
        dp_i = dp_i_1 + dp_i_2
        # 滚动更新
        dp_i_2 = dp_i_1
        dp_i_1 = dp_i
    return dp_i_1



"""
力扣第 322 题「零钱兑换」：

    给你 k 种面值的硬币，面值分别为 c1, c2 ... ck，每种硬币的数量无限，再给一个总金额 amount，问你最少需要几枚硬币凑出这个金额

1、确定「状态」，也就是原问题和子问题中会变化的变量。
    由于硬币数量无限，硬币的面额也是题目给定的，只有目标金额会不断地向 base case 靠近，
    所以唯一的「状态」就是目标金额 amount。
2、确定「选择」，也就是导致「状态」产生变化的行为。
    目标金额为什么变化呢，因为你在选择硬币，你每选择一枚硬币，就相当于减少了目标金额。
    所以说所有硬币的面值，就是你的「选择」。
3、明确 dp 函数/数组的定义。
    我们这里讲的是自顶向下的解法，所以会有一个递归的 dp 函数，
    一般来说函数的参数就是状态转移中会变化的量，也就是上面说到的「状态」；
    函数的返回值就是题目要求我们计算的量。
    就本题来说，状态只有一个，即「目标金额」，题目要求我们计算凑出目标金额所需的最少硬币数量。

"""

# 伪码框架
def coinChange(coins: List[int], amount: int) -> int:
    # 题目要求的最终结果是 dp(amount)
    return dp(coins, amount)

# 定义：要凑出金额 n，至少要 dp(coins, n) 个硬币
def dp(coins: List[int], n: int) -> int:
    # 做选择，选择需要硬币最少的那个结果
    # 初始化res为正无穷
    res = float('inf')
    for coin in coins:
        res = min(res, sub_problem + 1)
    return res


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 题目要求的最终结果是 dp(amount)
        return self.dp(coins, amount)

    # 定义：要凑出目标金额 amount，至少要 dp(coins, amount) 个硬币
    def dp(self, coins, amount):
        # base case
        if amount == 0: 
            return 0
        if amount < 0: 
            return -1

        res = float('inf')
        for coin in coins:
            # 计算子问题的结果
            subProblem = self.dp(coins, amount - coin)
            # 子问题无解则跳过
            if subProblem == -1: 
                continue
            # 在子问题中选择最优解，然后加一
            res = min(res, subProblem + 1)

        return res if res != float('inf') else -1

"""
状态定义：
dp(n) 表示凑出金额 n 所需的最少硬币数量。

状态转移方程：
- 如果 n == 0，说明不需要任何硬币，dp(n) = 0
- 如果 n < 0，说明无解，dp(n) = -1
- 如果 n > 0：
    dp(n) = min{ dp(n - coin) + 1 | coin ∈ coins 且 dp(n - coin) != -1 }
    即从所有能凑出 n - coin 的子问题中，选出最优的一个，再加上当前硬币 coin。
"""


class Solution:
    def __init__(self):
        self.memo = []
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = [-666] * (amount + 1)
        # 备忘录初始化为一个不会被取到的特殊值，代表还未被计算
        return self.dp(coins, amount)
    
    def dp(self, coins, amount):
        if amount == 0: return 0
        if amount < 0: return -1
        # 查备忘录，防止重复计算
        if self.memo[amount] != -666:
            return self.memo[amount]

        res = float('inf')
        for coin in coins:
            # 计算子问题的结果
            subProblem = self.dp(coins, amount - coin) 
            # 子问题无解则跳过
            if subProblem == -1: continue
            # 在子问题中选择最优解，然后加一
            res = min(res, subProblem + 1)
        # 把计算结果存入备忘录
        self.memo[amount] = res if res != float('inf') else -1
        return self.memo[amount]