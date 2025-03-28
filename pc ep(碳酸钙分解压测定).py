import math
import matplotlib.pyplot as plt
import numpy as np


a = []
b = []
c = []
z = []
p2 = float(input('输入第二次抽真空后压差值：'))

for i in range(1, 9):
    # 温度计算区
    t = float(input("请输入第{}组摄氏度数据：".format(i)))
    T = 273.15 + t
    y = 1 / T * 1000
    # 压强计算区
    p1 = float(input("请输入第{}组压强差数据：".format(i)))
    # 计算分解压
    P = -p2 + p1
    # 计算平衡常数
    K = P / 100
    # 平衡常数自然对数值
    lnK = math.log(K)
    print('T=', T)
    print('1/T=', y)
    print('分解压：', P)
    print('lnK=', lnK)
    a.append(T)
    b.append(y)
    c.append(lnK)
    z.append(P)
print('T', a)
print('1/T*1000:', b)
print('P:', z)
print('lnK:', c)

'''b=[1.0223380872054388, 0.9978546125829467, 0.977373796608513, 0.9504348239319488, 0.9335760631097418, 
0.9064950369396727, 0.8879811747990942, 0.8671898712223041] c= [-2.8438699242447436, -2.1839135632765467, 
-1.8413699697813894, -1.5278579254416773, -1.2808538486618937, -0.9028810449642373, -0.5859084298903466, 
-0.257346872655708]

c = [-2.383795148419589, -2.061208773418776, -1.7248487639454284, -1.424203934193111, -1.0990123686894495,
     -0.8123812684836436, -0.46856466505148126, -0.14896415313995834]
b = [1.0318320177475109, 1.0018534288433603,
     0.977373796608513, 0.9558858672274531, 0.9327053117567503, 0.9106224104175203, 0.8911464599206879,
     0.8694518106333956]
'''
# 线性回归模块

data = np.array(c)  # 这里只是示例，你应该用你的数据替换这
x = np.array(b)  # 这里的x值只是示例，你应该用你的x值替换这些
y = data  # 这里的y值只是示例，你应该用你的y值替换这些
# 计算直线的斜率
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x_squared = np.sum(x ** 2)
sum_xy = np.sum(x * y)
slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
intercept = np.mean(y) - slope * np.mean(x)
print('The slope of the line is:', slope)
print('截距为：', intercept)
H = -slope * 8.314
print('碳酸钙分解热为：{}kJ/mol'.format(H))
T3 = (-slope / intercept) * 1000
T4 = T3 - 273.15
print('碳酸钙在100kpa下的分解温度为：{}K，{}℃'.format(T3, T4))
# 绘图模块

e = np.array(b)
f = np.array(c)

# 进行线性拟合
coefficients = np.polyfit(e, f, 1)

# 创建一个表示拟合线性的函数
fit_function = np.poly1d(coefficients)

# 生成一些用于绘图的x值
x_plot = np.linspace(0, 12, 100)

# 使用拟合函数计算对应的y值
y_plot = fit_function(x_plot)

# 绘制原始数据点
plt.scatter(x, y)

ax = plt.subplot()
ax.spines['top'].set_visible(False)  # 设置坐标轴,下同
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position(('data', 0))
# 改变x轴和y轴的分度值
plt.xticks(np.arange(0, 1.5, step=0.005, ))  # 以0.5为步长设置x轴分度值
plt.yticks(np.arange(-3, 12, step=0.05))  # 以0.2为步长设置y轴分度值
# 绘制拟合线
plt.plot(x_plot, y_plot)
plt.grid(True)
plt.title('lnK-1/T figure')

plt.xticks(rotation=-45)
plt.xlabel('1/Tx10^3 / 1/K', labelpad=-50)
plt.ylabel('lnK')
plt.show()
