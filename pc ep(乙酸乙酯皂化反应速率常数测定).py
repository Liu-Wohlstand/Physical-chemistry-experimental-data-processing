import numpy as np
import matplotlib.pyplot as plt

'''lxs
Kt = np.array([1796, 1611, 1483, 1390, 1320, 1264, 1179, 1125, 1081])
K0 = 2150
K_infinite = 818
n=5
'''
'''wxw
Kt = np.array([1786, 1583, 1465, 1377, 1309, 1258, 1184, 1132, 1092])
K0 = 2160
K_infinite = 823
n=9
'''
'''dst
Kt = np.array([1821,1636,1507,1414,1344,1289,1208,1152,1110])
K0 = 2160
K_infinite = 826'''
'''zrl
Kt = np.array([1855,1667,1536,1441,1369,1311,1228,1171,1129])
K0 = 2210
K_infinite = 820'''
Kt = np.array([1506, 1305, 1167, 1075, 1009, 952, 876, 825, 788])
K0 = 2000
K_infinite = 760
n = 5  # 拟合数据数

# -------------------------------------------分割线以下勿改---------------------------------------------------------------
c = 0.01
bi = (K0 - Kt) / (Kt - K_infinite)
t = np.array([5, 10, 15, 20, 25, 30, 40, 50, 60])
K0_Kt = K0 - Kt
Kt_K_infinite = Kt - K_infinite

# 取前n个元素
t_1 = t[:n]
bi_1 = bi[:n]

for i in range(9):
    t_val = t[i]
    v = bi[i]
    a = K0_Kt[i]
    b = Kt_K_infinite[i]
    print(f't={t_val}min时，K0-Kt={a}，\nKt-K_infinite={b}，\n(K0 - Kt) / (Kt - K_infinite)={v}')

print()


def zhixiannihe(x, y):
    coefficients = np.polyfit(x, y, 1)
    fit_function = np.poly1d(coefficients)
    x_plot = np.linspace(0, 70, 100)
    y_plot = fit_function(x_plot)
    return x_plot, y_plot


def linear_regression(x, y):
    len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    numerator = sum((x - x_mean) * (y - y_mean))
    denominator = sum((x - x_mean) ** 2)
    b1 = numerator / denominator
    b0 = y_mean - b1 * x_mean
    return b0, b1


x_plot, y_plot = zhixiannihe(t_1, bi_1)
b, m = linear_regression(t_1, bi_1)
print(f"斜率为{m},截距为{b}")
print()
k = m / c
print(f'k={k} L/(mol*min)')
print()
banshuaiqi = 1 / (c * k)
print(f'半衰期为{banshuaiqi}min')
plt.plot(x_plot, y_plot)
plt.scatter(t, bi)
plt.xlabel('t (min)')
plt.ylabel('(K0 - Kt) / (Kt - K∞)')
plt.title('(K0-Kt)/(Kt-K∞) - t figure')

plt.text(30, 1.46, f'y={m:.4f}x+{b:.4f}')

plt.xlim(0, 65)
plt.ylim(0)
plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],
           ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60'])
plt.grid(True)
plt.show()
