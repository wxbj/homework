import random


def dynamic_programming(n, b, W, V):
    """
    :param n: 物品数
    :param b: 重量
    :param W: 每个物品的重量
    :param V: 每个物品的价值
    :return: 选择的物品
    """
    F = [[0 for _ in range(b + 1)] for _ in range(n)]
    I = [[0 for _ in range(b + 1)] for _ in range(n)]
    X = [0 for _ in range(n)]

    for k in range(n):
        for x in range(b + 1):
            if k == 0:
                if x < W[k]:
                    F[k][x] = 0
                    I[k][x] = 0
                else:
                    F[k][x] = V[k]
                    I[k][x] = 1
            elif x >= W[k] and V[k] + F[k - 1][x - W[k]] >= F[k - 1][x]:
                F[k][x] = V[k] + F[k - 1][x - W[k]]
                I[k][x] = 1
            else:
                F[k][x] = F[k - 1][x]
                I[k][x] = 0

    x = b
    for k in range(n - 1, -1, -1):
        if I[k][x] == 1:
            X[k] = 1
            x = x - W[k]
        else:
            X[k] = 0
    return X


if __name__ == "__main__":
    n = 100
    b = 1000
    W = [random.randint(0, 100) for _ in range(100)]
    V = [random.randint(0, 100) for _ in range(100)]
    # n = 4
    # b = 10
    # W = [2, 3, 4, 7]
    # V = [1, 3, 5, 9]
    print(dynamic_programming(n, b, W, V))
