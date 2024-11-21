# 改进欧拉法（梯形公式校正）
# 方程：di/dt = -R1*i, f0 = 0.05
# 采样点：nPoint=50

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示符号

R1 = 1000000  # 火花塞电阻
R = 100  # 电阻
U = 5  # 初始电压
f0 = U / R  # 初始值


# 方程
def f(t, i):
    return - R1 * i


# 四阶Runge-Kutta求解
def runge_kutta_4(f, i0, t_vals, h):
    i_vals = [i0]

    for t in t_vals[:-1]:
        i = i_vals[-1]
        k1 = h * f(t, i)
        k2 = h * f(t + h / 2, i + k1 / 2)
        k3 = h * f(t + h / 2, i + k2 / 2)
        k4 = h * f(t + h, i + k3)
        i_next = i + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        i_vals.append(i_next)

    return np.array(i_vals)


# 参数设置
t0 = 0  # 初始时间
i0 = 0.05  # 初始电流
h = 1e-6  # 步长

# 时间点
nPoint = 50
t = np.linspace(0, 0.02 * 10, nPoint)

# 计算结果
i_vals = runge_kutta_4(f, i0, t, h)

# 绘制图像
plt.figure(figsize=(12, 6))

# 电流i(t)图像
plt.subplot(2, 1, 1)
plt.plot(t, i_vals, label='Current i(t)')
plt.xlabel('Time (t)')
plt.ylabel('Current (i(t))')
plt.legend()

# 电压u(t)图像
plt.subplot(2, 1, 2)
plt.plot(t, i_vals * R1, label='Voltage u(t)', color='r')
plt.xlabel('Time (t)')
plt.ylabel('Voltage (u(t))')
plt.legend()

plt.tight_layout()
plt.show()
