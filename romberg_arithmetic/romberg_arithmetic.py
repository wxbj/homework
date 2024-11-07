import math


# 龙贝格（Romberg)算法主逻辑
def romberg_arithmetic(f, a, b, wrong_number):
    # T用来存储中间结果
    T = [((b - a) / 2) * (f(a) + f(b))]
    k = 1
    # 递推公式
    while True:
        sum = 0
        for i in range(1, 2 ** (k - 1) + 1):
            sum = sum + f(a + ((2 * i - 1) * (b - a)) / (2 ** k))
        T.append((T[k - 1] / 2) + ((b - a) * sum) / (2 ** k))
        if T[k] - T[k - 1] < (3 * wrong_number):
            break
        k = k + 1
    return 2 ** k, T[k]


# 被积函数
def function(x):
    if x == 0:
        return 1
    else:
        return math.sin(x) / x


if __name__ == "__main__":
    #  积分下限
    a = 0
    # 积分上限
    b = 1
    # 误差
    error = 0.5 * 10 ** -6
    # 所需节点数和近似值
    node_number, result = romberg_arithmetic(function, a, b, error)
    print(node_number, result)
