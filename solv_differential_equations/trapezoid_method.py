# 改进欧拉法（梯形公式校正）
# 方程：dy/dt = -100y, y(0) = 1
# 采样点：nPoint=50


import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示符号


def backward_euler(f, y0, t, tol=1e-6, max_iter=1):
    """
    后退欧拉法求解常微分方程初值问题

    参数:
    f -- 微分方程的右侧函数
    y0 -- 初始值
    t -- 时间点数组
    tol -- 容忍度
    max_iter -- 最大迭代次数

    返回:
    y -- 在时间点t上的解的数组
    """
    n = len(t)
    y = np.zeros(n)
    y[0] = y0

    for i in range(1, n):
        # 迭代初值
        y[i] = y[i - 1] + f(t[i - 1], y[i - 1]) * (t[i] - t[i - 1])
        # 使用固定点迭代求解梯形公式
        y_new = y[i]
        j = 0
        for _ in range(max_iter):
            j += 1
            y_old = y_new
            y_new = y[i - 1] + (f(t[i - 1], y[i - 1]) + f(t[i], y_new)) * (t[i] - t[i - 1]) / 2
            if abs(y_new - y_old) < tol:
                print(j)
                break
        y[i] = y_new
    return y


def f(t, y):
    return -100 * y


def y(x):
    return np.exp(-100 * x)


# 时间点
nPoint = 50
t = np.linspace(0, 0.02 * 10, nPoint)
# 初始值
y0 = 1

# 求解
y_backward_euler = backward_euler(f, y0, t)
print(y_backward_euler)
# 绘制结果
plt.plot(t, y_backward_euler, 'or', label='改进欧拉法')
plt.plot(np.linspace(0, 0.02 * 10, nPoint), y(np.linspace(0, 0.02 * 10, nPoint)), '*b', label='精确解')

plt.legend()
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('Backward Euler Method')
plt.show()
