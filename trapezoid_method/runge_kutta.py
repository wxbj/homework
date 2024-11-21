# runge_kutta
# 方程：di/dt = -R1*i, f0 = 0.05
# 采样点：nPoint=50

import numpy as np
import matplotlib.pyplot as plt

# 参数设置
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示符号

R1 = 1000000  # 火花塞电阻
R = 100  # 电阻
U = 5  # 初始电压
f0 = U / R  # 初始值
h = 1e-6  # 步长

# 方程
def f(t, i):
    return - R1 * i


# 四阶Runge-Kutta求解
def runge_kutta_4(f, f0, t_vals, h):
    i_vals = [f0]

    for t in t_vals[:-1]:
        i = i_vals[-1]
        k1 = h * f(t, i)
        k2 = h * f(t + h / 2, i + k1 / 2)
        k3 = h * f(t + h / 2, i + k2 / 2)
        k4 = h * f(t + h, i + k3)
        i_next = i + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        i_vals.append(i_next)

    return np.array(i_vals)


# 时间点
nPoint = 50
t = np.linspace(0, 0.02 * 10, nPoint)

# 计算结果
i_vals = runge_kutta_4(f, f0, t, h)

# 绘制图像
plt.figure(figsize=(12, 6))

# 电流i(t)图像
plt.subplot(2, 1, 1)
plt.plot(t, i_vals, 'or', label='电流随时间变化图', color='b')
plt.xlabel('t')
plt.ylabel('i')
plt.legend()

# 电压u(t)图像
plt.subplot(2, 1, 2)
plt.plot(t, i_vals * R1, 'or', label='电压随时间变化图', color='r')
plt.xlabel('t')
plt.ylabel('u')
plt.legend()

plt.tight_layout()
plt.show()
