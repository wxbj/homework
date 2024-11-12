from collections import deque
import random


# 动态规划
def dynamic_programming_use_pretreatment(n, b, W, V, pretreatment_list):
    F = [[0 for _ in range(b + 1)] for _ in range(n)]
    I = [[0 for _ in range(b + 1)] for _ in range(n)]
    X = [0 for _ in range(n)]

    for k, pretreatment_set in zip(range(len(pretreatment_list)), pretreatment_list):
        for x in pretreatment_set:
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


# 预处理，获取需要计算的值的序号
def pretreatment(n, b, W):
    my_list = []
    for i in range(n):
        my_list.append([])
    queue = deque()
    sign = [[0 for _ in range(b + 1)] for _ in range(n)]

    queue.append(n - 1)
    queue.append(b)

    for i in range(n - 1, -1, -1):
        while queue[0] == i:
            if sign[queue[0]][queue[1]] == 0:
                j = queue.popleft()
                k = queue.popleft()
                my_list[j].append(k)
                sign[j][k] = 1
                if k - W[j] > 0 and j > 0:
                    queue.append(j - 1)
                    queue.append(k - W[j])
                queue.append(j - 1)
                queue.append(k)
            else:
                queue.popleft()
                queue.popleft()

    length = []
    for i in my_list:
        length.append(len(i))
    print(length)
    # print(my_list)
    return my_list


if __name__ == "__main__":
    n = 500
    b = 10000
    W = [random.randint(0, 100) for _ in range(500)]
    V = [random.randint(0, 100) for _ in range(500)]
    print(V)
    # n = 4
    # b = 10
    # W = [2,3,4,7]
    # V = [1,3,5,9]
    print(dynamic_programming_use_pretreatment(n, b, W, V, pretreatment(n, b, W)))
