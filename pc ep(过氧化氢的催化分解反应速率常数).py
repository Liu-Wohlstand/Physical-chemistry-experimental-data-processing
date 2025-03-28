import numpy as np
import matplotlib.pyplot as plt

'''刘兴盛
t1 = ['0.43.40', '1.52.18', '2.46.15', '3.42.74', '4.41.55', '5.43.12', '6.49.99', '8.01.37', '9.22.46', '10.47.96']
t2 = ['0.15.18', '0.46.90', '1.11.96', '1.36.40', '2.02.09', '2.26.80', '2.52.21', '3.19.52', '3.46.18', '4.14.34']
t3 = ['0.42.12', '1.44.90', '2.33.58', '3.22.55', '4.13.21', '5.05.74', '6.03.77', '6.49.43', '7.43.40', '8.38.18']
'''
'''zrl
t1 = ['0.49.77', '1.41.33', '2.34.74', '3.27.52', '4.26.39', '5.26.58', '6.31.80', '7.44.18', '9.02.02', '10.28.30']
t2 = ['0.43.63', '1.12.17', '1.37.83', '2.01.98', '2.28.05', '2.53.20', '3.19.11', '3.45.52', '4.13.39', '4.41.48']
t3 = ['1.05.43', '1.54.71', '2.41.24', '3.28.52', '4.17.27', '5.06.15', '5.56.83', '6.49.80', '7.43.65', '8.39.08']

'''
'''汪显伟
t1 = ['0.50.43', '1.40.43', '2.31.05', '3.23.99', '4.17.71', '5.21.52', '6.24.21', '7.35.15', '8.49.58', '10.18.43']
t2 = ['0.31.24', '0.56.12', '1.18.27', '1.42.30', '2.04.59', '2.28.37', '2.52.65', '3.17.62', '3.44.37', '4.11.09']
t3 = ['0.53.62', '1.36.47', '2.20.46', '3.06.34', '3.50.77', '4.36.06', '5.25.09', '6.20.96', '7.13.68', '8.07.24']

R = 8.314
c_h2o2 = 1.5768
V_h2o2 = np.array([5, 10])
t = 20
p_atom = 101.02
p_H2O = 2.3378
'''
'''栾和盛
t1 = ['1.07.05', '2.05.33', '2.58.27', '3.55.14', '4.52.27', '5.54.92', '7.04.89', '8.17.17', '9.35.30', '11.02.39']
t2 = ['0.32.55', '1.02.05', '1.28.24', '1.53.52', '2.18.77', '2.44.68', '3.09.74', '3.36.40', '4.03.00', '4.30.52']
t3 = ['1.05.86', '1.57.08', '2.40.61', '3.31.89', '4.23.20', '5.12.14', '6.06.58', '7.03.02', '7.57.52', '8.55.55']
'''
'''lql
t1 = ['0.32.59',  '1.23.56', '2.16.16', '3.11.88', '4.10.10', '5.06.76', '6.06.76', '7.18.01', '8.13.76', '9.52.79']
t2 = ['0.18.53', '0.41.81', '1.04.84', '1.28.02', '1.54.65', '2.14.03', '2.38.84', '3.03.34', '', '3.23,40','3.56.15']
t3 = ['0.39.69', '1.27.54', '2.11.20', '3.03.17', '3.51.48', '4.37.83', '5.26.99', '6.17.80', '7.10.49', '8.07.21']
'''
'''dst 
t1 = ['00.48.72', '1.51.21', '02.59.73', '03.51.16', '04.50.10', '05.43.55', '06.51.73', '8.2.96', '9.19.78', 
'10.38.58'] 
t2 = ['0.40.67', '1.8.46', '1.33.62', '1.57.67', '2.22.21', '2.46.32', '3.11.98', '3.38.00', '4.06.35', 
'4.33.37'] 
t3 = ['0.59.69', '1.51.42', '2.42.39', '3.28.04', '4.17.61', '5.08.96', '5.59.24', '6.53.69', '7.49.39', 
'8.47.73']
'''
t1 = ['0.50.43', '1.40.43', '2.31.05', '3.23.99', '4.17.71', '5.21.52', '6.24.21', '7.35.15', '8.49.58', '10.18.43']
t2 = ['0.31.24', '0.56.12', '1.18.27', '1.42.30', '2.04.59', '2.28.37', '2.52.65', '3.17.62', '3.44.37', '4.11.09']
t3 = ['0.53.62', '1.36.47', '2.20.46', '3.06.34', '3.50.77', '4.36.06', '5.25.09', '6.20.96', '7.13.68', '8.07.24']
c_h2o2 = 1.5768
t = 18.8
p_atom = 100.93
p_H2O = 2.1694

# -------------------------------------------分割线以下勿改---------------------------------------------------------------
R = 8.314
V_h2o2 = np.array([5, 10])
p = p_atom - p_H2O
V_infinite = c_h2o2 * V_h2o2 * 10 ** (-3) * R * (t + 273.15) / (2 * p * 10 ** 3) * 1000000
V_t = np.arange(5, 55, 5)
t1_convert = []
t2_convert = []
t3_convert = []
V_infinite1 = V_infinite[0]
V_infinite2 = V_infinite[1]
y1 = np.log(V_infinite1 - V_t)
y2 = np.log(V_infinite2 - V_t)

print(f'5mL H2O2 V无穷={V_infinite[0]}mL,\n10mL H2O2 V无穷={V_infinite[1]}mL')
print()
for t, v in zip(y1, V_t):
    print(f'H2O2=5mL时 Vt={v} mL时，ln(V∞-Vt)={t}')
print()
for t, v in zip(y2, V_t):
    print(f'H2O2=10mL 时Vt={v} mL时，ln(V∞-Vt)={t}')
print()


def convert_time_to_minutes(time_str):
    # 分割时间字符串为分钟、秒和小数秒部分
    parts = time_str.split('.')
    if len(parts) != 3:
        raise ValueError("输入的时间格式不正确，应为 分钟.秒.小数秒")

        # 提取并转换分钟、秒和小数秒为浮点数
    minutes = float(parts[0])
    seconds = float(parts[1])
    decimal_seconds = float('.' + parts[2])

    # 计算总秒数并转换为分钟
    total_seconds = minutes * 60 + seconds + decimal_seconds
    total_minutes = total_seconds / 60

    return total_minutes


for i in t1:
    t1_1 = convert_time_to_minutes(i)
    t1_convert.append(t1_1)

for i in t2:
    t2_1 = convert_time_to_minutes(i)
    t2_convert.append(t2_1)

for i in t3:
    t3_1 = convert_time_to_minutes(i)
    t3_convert.append(t3_1)

for t, v in zip(t1_convert, V_t):
    print(f'第一组Vt={v} mL时，t1={t} min')
print()
for t, v in zip(t2_convert, V_t):
    print(f'第二组Vt={v} mL时，t1={t} min')
print()
for t, v in zip(t3_convert, V_t):
    print(f'第三组Vt={v} mL时，t1={t} min')
print()

t1_convert = np.array(t1_convert)
t2_convert = np.array(t2_convert)
t3_convert = np.array(t3_convert)


def linear_regression(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    numerator = sum((x - x_mean) * (y - y_mean))
    denominator = sum((x - x_mean) ** 2)

    b1 = numerator / denominator
    b0 = y_mean - b1 * x_mean

    return b0, b1


t1__nihe_k, y1__nihe_b = linear_regression(t1_convert, y1)
t2__nihe_k, y2__nihe_b = linear_regression(t2_convert, y2)
t3__nihe_k, y3__nihe_b = linear_regression(t3_convert, y2)
print(f't1斜率为{y1__nihe_b}\nt2斜率为{y2__nihe_b}\nt3斜率为{y3__nihe_b}')
print()
t1_half = -np.log(2) / y1__nihe_b
t2_half = -np.log(2) / y2__nihe_b
t3_half = -np.log(2) / y3__nihe_b
print(f'第一组实验半衰期为{t1_half}min\n第二组实验半衰期为{t2_half}min\n第三组实验半衰期为{t3_half}min')
print()


def zhixiannihe(x, y):
    coefficients = np.polyfit(x, y, 1)
    fit_function = np.poly1d(coefficients)
    x_plot = np.linspace(min(x), max(x), 100)
    y_plot = fit_function(x_plot)
    return x_plot, y_plot


t1nihe, y1nihe = zhixiannihe(t1_convert, y1)
t2nihe, y2nihe = zhixiannihe(t2_convert, y2)
t3nihe, y3nihe = zhixiannihe(t3_convert, y2)
# 绘制原始数据点
plt.scatter(t1_convert, y1, marker='^', label='25mL 0.1000mol/L KI + 5mL H2O2 + 5mL H2O')
plt.scatter(t2_convert, y2, marker='v', label='25mL 0.1000mol/L KI + 10mL H2O2')
plt.scatter(t3_convert, y2, marker='*', label='25mL 0.0500mol/L KI + 10mL H2O2')
plt.legend(loc='lower left')

# 绘制拟合线
plt.plot(t1nihe, y1nihe, label='25mL 0.1000mol/L KI + 5mL H2O2 + 5mL H2O')
plt.plot(t2nihe, y2nihe, label='25mL 0.1000mol/L KI + 10mL H2O2')
plt.plot(t3nihe, y2nihe, label='25mL 0.0500mol/L KI + 10mL H2O2')

# 绘点区
plt.text(2, 4.148, f'y={y1__nihe_b:.3f}x+{t1__nihe_k:.3f}')
plt.text(1, 4.918, f'y={y2__nihe_b:.3f}x+{t2__nihe_k:.3f}')
plt.text(7, 5.148, f'y={y3__nihe_b:.3f}x+{t3__nihe_k:.3f}')

plt.grid(True)
plt.title('ln(V∞-Vt)-t figure')
plt.xlabel('t /min')
plt.ylabel('ln(V∞-Vt/mL)')
# 调整分度值
xlim_min, xlim_max = 0, max(t1_convert)
plt.xticks(np.arange(0, xlim_max + 2, 1))
plt.xlim(0, xlim_max + 2)
ylim_min, ylim_max = 3, 6.1
plt.ylim(3, 6)
plt.yticks(np.arange(ylim_min, ylim_max, 0.1))
plt.yticks([3, 4, 5, 6], ['3', '4', '5', '6'])

locator = plt.MaxNLocator(nbins=100)  # 这里设置10个大致均匀分布的刻度线
plt.gca().yaxis.set_major_locator(locator)

plt.show()
