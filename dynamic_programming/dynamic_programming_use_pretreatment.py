from collections import deque
import random


# 动态规划
def dynamic_programming_use_pretreatment(n, b, W, V, pretreatment_list):
    # F[n][b+1]所求函数，I[n][b+1]标记函数，X[n]最终输出的0-1向量
    F = [[0 for _ in range(b + 1)] for _ in range(n)]
    I = [[0 for _ in range(b + 1)] for _ in range(n)]
    X = [0 for _ in range(n)]

    # 这里遍历传进来的变长数组
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
    # 根据标记记录装入情况
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
    # my_list[n][]为我们最后需要求的边长2维数组
    my_list = []
    for i in range(n):
        my_list.append([])

    # 利用sign[n][b+1]来去重,0表示没存储过，1表示已经存储过了
    sign = [[0 for _ in range(b + 1)] for _ in range(n)]

    # 利用队列来处理每一个物品：物品1，最大重量1，物品2，最大重量2
    queue = deque()
    queue.append(n - 1)
    queue.append(b)

    # 遍历每一个物品
    for i in range(n - 1, -1, -1):
        # 如果队列中还是这个物品的话
        while queue[0] == i:
            # 判断是否存储过
            if sign[queue[0]][queue[1]] == 0:
                # 没存储过，则出队两个元素：物品j，最大重量k
                j = queue.popleft()
                k = queue.popleft()
                # 将物品J的需要算的最大重量加入变长数组
                my_list[j].append(k)
                # 设置为存储过
                sign[j][k] = 1
                # 背包有容量则将F[j-1][k - W[j]入队
                if k > W[j]:
                    queue.append(j - 1)
                    queue.append(k - W[j])
                # 将F[j-1][k]入队
                queue.append(j - 1)
                queue.append(k)
            else:
                # 存储过直接弹出，然后处理下两个数据
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
    W = [random.randint(1, 100) for _ in range(500)]
    print(W)
    V = [random.randint(1, 100) for _ in range(500)]
    print(V)
    # n = 4
    # b = 10
    # W = [2, 3, 4, 7]
    # V = [1, 3, 5, 9]
    print(dynamic_programming_use_pretreatment(n, b, W, V, pretreatment(n, b, W)))
