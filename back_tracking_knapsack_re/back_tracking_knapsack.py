import random

size = 30  # 物品数量
B = 0  # 界限
cv = 0  # 当前价值
cw = 0  # 当前重量
X = [0 for _ in range(size)]  # 记录是否放入物品
Y = [0 for _ in range(size)]  # 临时记录是否放入物品


def BackTrackingKnapsack(n, b, W, V):
    global B, cv, cw, X, Y
    i = 0
    while True:
        C = Cost(i, n, V)
        if C > B:
            i = i + 1
            if (cw + W[i]) <= b:
                cv = cv + V[i]
                cw = cw + W[i]
                X[i] = 1
            else:
                X[i] = 0
        else:
            i = Back(i, V, W)
        if i == n - 1:
            if cv > B:
                B = cv
                Y = X.copy()
            i = Back(n - 1, V, W)
        if i == 0:
            return "\n    选择的物品序号：" + str(Y) + "\n    最终装入背包的价值：" + str(B)


# 代价函数
def Cost(i, n, V):
    global cv
    c = cv
    for j in range(i + 1, n):
        c = c + V[j]
    return c


def Back(i, V, W):
    global cv, cw
    while True:
        if i == 1 and X[i] == 0:
            return 0
        if X[i] == 1:
            cv -= V[i]
            cw -= W[i]
            if i < n:
                X[i] = 0
                return i
            else:
                i = i - 1
        else:
            i = i - 1


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
    print("结果：", BackTrackingKnapsack(n, b, W, V))
