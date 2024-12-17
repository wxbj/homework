import random

size = 30  # 物品数量
B = 0  # 界限
cv = 0  # 当前价值
cw = 0  # 当前重量
X = [0 for _ in range(size)]  # 记录是否放入物品
Y = [0 for _ in range(size)]  # 临时记录是否放入物品
count = 0  # 统计递归轮数


def BackTrackingKnapsackRe(n, b, W, V):
    return BTKR(n, b, W, V, 0)


# 递归回溯回溯程序
def BTKR(n, b, W, V, s):
    global B, cv, cw, X, count, Y
    count += 1
    if cw > b or cost(s, n, V) <= B: return 0
    if cv > B:
        B = cv
        Y = X.copy()
    i = s
    while i < n:
        cv = cv + V[i]
        cw = cw + W[i]
        X[i] = 1
        BTKR(n, b, W, V, i + 1)
        cv = cv - V[i]
        cw = cw - W[i]
        X[i] = 0
        i = i + 1
    return "\n    选择的物品序号：" + str(Y) + "\n    最终装入背包的价值：" + str(B)


# 代价函数
def cost(i, n, V):
    global cv
    c = cv
    for j in range(i + 1, n):
        c = c + V[j]
    return c


if __name__ == "__main__":
    # n = 4
    # b = 13
    # V = [12, 11, 9, 8]
    # W = [8, 6, 4, 3]
    n = size
    b = 10 * size
    V = [random.randint(0, 100) for _ in range(size)]
    W = [random.randint(0, 100) for _ in range(size)]
    print("物品数量：", size)
    print("物品价值：", V)
    print("物品重量：", W)
    print("结果：", BackTrackingKnapsackRe(n, b, W, V))
    print("回溯法需要的递归次数：", count)
    print("暴力算需要遍历的数量：", 2 ** size)
