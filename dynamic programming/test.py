from collections import deque


# 动态规划
def dynamic_programming_use_pretreatment(n, b, W, V, pretreatment_list):
    F = [[0 for _ in range(b + 1)] for _ in range(n + 1)]
    I = [[0 for _ in range(b + 1)] for _ in range(n + 1)]
    X = [0 for _ in range(n + 1)]
    for k, my_set in zip(range(len(pretreatment_list)), pretreatment_list):
        for x in my_set:
            if x >= W[k] and V[k] + F[k - 1][x - W[k]] >= F[k - 1][x]:
                F[k][x] = V[k] + F[k - 1][x - W[k]] >= F[k - 1][x]
                I[k][x] = 1
            else:
                F[k][x] = F[k - 1][x]
                I[k][x] = 0

    x = b
    for k in range(n, 0, -1):
        if I[k][x] == 1:
            X[k] = 1
            x = x - W[k]
        else:
            X[k] = 0
    print(X[1:])


# 预处理，获取需要计算的值的序号
def pretreatment(n, b, W):
    my_list = []
    queue = deque()
    for i in range(n + 1):
        my_list.append(set())
    queue.append(n)
    queue.append(b)
    for i in range(n, 0, -1):
        while True:
            j = queue.popleft()
            k = queue.popleft()
            if k > 0:
                my_list[j].add(k)
                queue.append(j - 1)
                queue.append(k - W[j])
            queue.append(j - 1)
            queue.append(k)
            if queue[0] != i:
                break
    # [set(), {0, 3, 6, 7, 10}, {0, 10, 3, 6}, {10, 3}, {10}]
    return my_list


if __name__ == "__main__":
    n = 4
    b = 10
    W = [0, 2, 3, 4, 7]
    V = [0, 1, 3, 5, 9]
    dynamic_programming_use_pretreatment(n, b, W, V, pretreatment(n, b, W))
