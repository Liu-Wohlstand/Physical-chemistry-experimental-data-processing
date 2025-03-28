import numpy as np

p0 = 606 #0.0mol/L
p = np.array([589, 567.5, 538.75, 516.5, 495])


# 转换系数K
K = 73.34 * 10 **(-3) / p0
# 计算表面张力数组
r = K * p/1000
# 浓度数组
c = np.array([0.1, 0.2, 0.4, 0.6, 0.8])

# 打印K的值
print(f'K={K}')

# 假设c和p数组的长度相同，且按顺序对应
for i in range(len(c)):
    print(f'{c[i]} mol/L乙醇的表面张力大小为 {r[i]}*10^3 N·m-1')

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 定义拟合函数
def func(c, a, b):
    return 73.34 - 73.34 * a * np.log(1 + c / b)

# 使用curve_fit进行拟合
popt, pcov = curve_fit(func, c, r)

a, b = popt

# 打印拟合得到的a和b值
print(f'a={a}, b={b}')

# 绘制图像
plt.scatter(c, r, label='Data')
plt.plot(c, func(c, a, b), 'r-', label='Fitted Curve')
plt.xlabel('c (mol/L)')
plt.ylabel('r (N·m-1)')
plt.legend()
plt.show()