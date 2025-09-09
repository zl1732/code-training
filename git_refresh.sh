git config --global --unset http.proxy
git config --global --unset https.proxy
git add . && git commit -m "add file"
git pull --rebase
git push origin main


# git fetch origin
# git reset --hard origin/main # 强制使用远程文件
# git merge origin/main --allow-unrelated-histories
# git add . && git commit -m "add file"
# git push origin main





# 第一个问题：merge vs rebase
# git fetch origin
# git merge origin/main
# A --- B --- B1 ------- M    <- 本地 main
#        \           /
#         C1 --- C2         <- origin/main
# M 是一个新的 merge commit

# 历史保留了双方的提交

# 缺点：有“分叉”和“合并”节点，历史不是完全直线

# 优点：安全、简单，最常用


# git fetch origin
# git rebase origin/main
# A --- B --- C1 --- C2 --- B1'    <- 本地 main
# B1' 是“重新应用”的提交（hash 会改变）

# 历史是 完全线性的

# 缺点：冲突多的时候比较麻烦，而且如果多人协作，强推会有风险

# 优点：提交历史干净整洁，便于回溯


# 第二个问题：
# 假设你本地修改了几个文件，但 还没有执行 git add 或 git commit，然后你执行：

# git fetch origin
# git merge origin/main


# 情况分析：

# fetch 是安全的

# git fetch 只是拉远程数据，不动工作区

# 本地未提交的修改完全不会受影响

# merge 的行为取决于冲突情况

# 如果你本地修改的文件 远程没有改 → 安全，本地修改保留 + 新文件合并进来

# 如果你本地修改的文件 远程也改了 → 会产生冲突，Git 会要求你手动解决

# Git 不会直接覆盖本地未提交的修改，除非你强制操作（比如 git reset --hard）