"""在先导图里找到拐点和平台坐标，替换示例数据的y数据和坐标"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

matplotlib.rc("font", family='YouYuan')


# 曲线拟合函数
def quxiannihehanshu1(x, y):
    p = np.polyfit(x, y, 2)
    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = np.polyval(p, x_fit)
    return x_fit, y_fit
#-----------------------以上请勿改动-----------------
# 绘制步冷曲线的数据
# Pb
y_Pb = np.array(
    [386.5,383.4,379.9,376.1,372.2,368.2,364.0,359.8,355.5,351.2,347.1,342.9,338.7,334.6,330.5,326.7,324.8,324.0,323.5,
     323.2,322.8,322.4,322.0,321.8,321.4,321.2,320.8,320.5,320.1,319.4,318.5,316.4,311.5,305.5,299.6,294.0,288.6,283.7,
     278.9,274.4])  # 纯铅
end_value = 20 * (len(y_Pb) - 1)
start_value = 0
x_Pb = np.arange(start_value, end_value + 1, 20)

# 30%Sn
y_30 = np.array(
    [331.6,324.7,316.7,309.0,302.0,295.6,289.5,283.6,278.3,268.6,264.4,260.8,257.6,254.8,252.4,248.6,246.9,245.1,243.4,
     241.6,239.8,238.1,236.3,234.6,232.5,231.0,229.3,227.6,225.7,224.0,222.3,220.3,218.5,216.7,214.8,212.9,211.1,209.3,
     207.4,205.6,203.8,202.1,200.3,198.6,197.0,195.2,193.6,191.9,190.3,188.7,187.1,185.5,184.1,183.4,183.3,183.4,183.4,
     183.4,183.4,183.4,183.3,183.3,183.3,183.3,183.2,183.1,183.0,182.9,182.6,182.4,182.1,181.7,181.1,180.3,179.0,176.3,
     173.0,169.6,166.4,163.3
     ])  # 30%Sny
start_value = end_value + 50
end_value = start_value + 20 * (len(y_30) - 1)
x_30 = np.arange(start_value, end_value + 1, 20)

# 61.9%
y_619 = np.array(
    [235.8,232.9,228.6,223.8,219.2,214.8,210.7,206.3,203.1,200.3,198.2,196.3,194.5,193.0,191.3,189.8,188.2,186.7,185.1,
     183.4,182.2,181.1,181.2,181.3,181.4,181.5,181.5,181.5,181.5,181.5,181.4,181.4,181.3,181.2,181.0,180.5,180.2,179.8,
     179.4,179.0,178.3,175.5,171.1,166.7,162.7,159.0,155.2,152.0])  # 61.9%y
start_value = end_value + 50
end_value = start_value + 20 * (len(y_619) - 1)
x_619 = np.arange(start_value, end_value + 1, 20)

# 80%
y_80 = np.array(
    [245.7,238.7,231.6,225.0,218.7,212.7,209.4,207.7,206.6,205.7,204.8,203.9,202.9,202.0,200.8,199.7,198.4,197.1,195.6,
     194.1,192.4,190.8,189.0,187.3,185.4,183.6,182.4,182.2,182.1,182.1,182.1,182.1,182.1,182.1,182.0,181.6,181.2,180.7,
     179.4,178.2,177.0,175.5,172.7,169.6,164.7,160.9,156.7,153.9])  # 80%y
start_value = end_value + 50
end_value = start_value + 20 * (len(y_80) - 1)
x_80 = np.arange(start_value, end_value + 1, 20)

# 纯Sn
y_Sn = np.array(
    [301.2,286.1,274.5,264.1,255.1,246.9,239.0,232.2,231.4,231.1,230.9,230.7,230.5,230.4,230.3,230.2,230.1,230.3,229.9,
     229.8,229.6,229.4,229.2,228.7,228.1,221.1,224.6,218.6,211.6,205.4,199.1,193.6,188.0,183.0,178.1,173.6])  # 纯Sny
start_value = end_value + 50
end_value = start_value + 20 * (len(y_Sn) - 1)
x_Sn = np.arange(start_value, end_value + 1, 20)

# 绘制相图所需数据
# 依次输入纯铅、30%锡、61.9%锡、80%锡、纯锡的拐点温度
a1 = 324.8
a2 = 248.6
a3 = 182.4
a4 = 209.4
a5 = 232.2

# 依次输入纯铅、30%锡、61.9%锡、80%锡、纯锡的拐点温度横坐标
c1 = 320
c2 = 1130
c3 = 2070
c4 = 3570
c5 = 4580
#-----------------------以下请勿改动-----------------
# 依次输入样品质量分数
b1 = 0.00
b2 = 30
b3 = 61.9
b4 = 80
b5 = 100
x_left = np.array([0.00, 30, 61.9])
y_left = np.array([a1, a2, a3])
x_right = np.array([61.9, 80, 100])
y_right = np.array([a3, a4, a5])
x_tpl = np.array([19.7, 97.4])
y_tpl = np.array([a3, a3])

# 画虚线

x_pb_pingtai = [c1, end_value+1000]
y_pb_pingtai = [a1, a1]
x_30_guaidian = [c2, end_value+1000]
y_30_guaidian = [a2, a2]
x_619_pingtai = [c3, end_value+1000]
y_619_pingtai = [a3, a3]
x_80_guaidian = [c4, end_value+1000]
y_80_guaidian = [a4, a4]
x_sn_pingtai = [c5, end_value+1000]
y_sn_pingtai = [a5, a5]

x_30_ax2_guaidain = [0, 30]
y_30_ax2_guaidain = y_30_guaidian
x_619_ax2_pingtai = [0, 19.7]
y_619_ax2_pingtai = y_619_pingtai
x_80_ax2_guaidain = [0, 80]
y_80_ax2_guaidain = y_80_guaidian
x_sn_ax2_pingtai = [0, 100]
y_sn_ax2_pingtai = y_sn_pingtai

x_pb_xian = np.linspace(x_Pb.min(), x_Pb.max(), 500)
f = make_interp_spline(x_Pb, y_Pb)
y_pb_xian = f(x_pb_xian)
# 曲线拟合
x_left_nihe, y_left_nihe = quxiannihehanshu1(x_left, y_left)
x_right_nihe, y_right_nihe = quxiannihehanshu1(x_right, y_right)

# 提取x和y中对应索引的数据30%
x_30_xian = np.linspace(x_30.min(), x_30.max(), 500)
f = make_interp_spline(x_30, y_30)
y_30_xian = f(x_30_xian)

# 提取x和y中对应索引的数据61.9%
x_619_xian = np.linspace(x_619.min(), x_619.max(), 500)
f = make_interp_spline(x_619, y_619)
y_619_xian = f(x_619_xian)

# 提取x和y中对应索引的数据80%
x_80_xian = np.linspace(x_80.min(), x_80.max(), 500)
f = make_interp_spline(x_80, y_80)
y_80_xian = f(x_80_xian)

# 提取x和y中对应索引的数据Sn
x_sn_xian = np.linspace(x_Sn.min(), x_Sn.max(), 500)
f = make_interp_spline(x_Sn, y_Sn)
y_sn_xian = f(x_sn_xian)
# 图绘制区

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, gridspec_kw={'hspace': 0.5})

# 步冷曲线图绘制区
# Pb线
ax1.plot(x_pb_xian, y_pb_xian, color='blue', label='Pb')

ax1.scatter(x_Pb, y_Pb, color='blue', s=2)

# 30%线
ax1.plot(x_30_xian, y_30_xian, color='cyan', label='30%Sn')

ax1.scatter(x_30, y_30, color='cyan', s=2)

# 61.9%线
ax1.plot(x_619_xian, y_619_xian, color='green', label='61.9%Sn')
ax1.scatter(x_619, y_619, color='green', s=2)

# 80%线
ax1.plot(x_80_xian, y_80_xian, color='orange', label='80%Sn')

ax1.scatter(x_80, y_80, color='orange', s=2)

# Sn线
ax1.plot(x_sn_xian, y_sn_xian, color='purple', label='Sn')

ax1.scatter(x_Sn, y_Sn, color='purple', s=2)

# 设置标题和轴标签
ax1.set_title('图1 Pb-Sn系统步冷曲线')
ax1.set_xlabel('t/s')
ax1.set_ylabel('T/℃')

'''ax1.set_xticks(np.arange(min(x), max(x) + 1, 1))'''
# ax1.set_yticks(np.arange(150, 360, 25))
ax1.grid(True)  # 显示网格线
ax1.spines['right'].set_visible(False)
ax1.legend()  # 添加图例

# 相图绘图区
ax2.plot(x_left_nihe, y_left_nihe)
ax2.plot(x_right_nihe, y_right_nihe)
ax2.scatter(x_left, y_left)
ax2.scatter(x_right, y_right)
ax2.plot(x_tpl, y_tpl)
ax2.set_title('图2 Pb-Sn系统相图')
ax2.set_xlabel('w(Sn%)')
ax2.set_ylabel('T/℃')
ax2.set_yticks(np.arange(100, 360, 10))

# 强制设定轴长度
ylim_min, ylim_max = 100, 360  # y轴的范围，假设这个范围可以覆盖两个函数的最大最小值
ax1.set_ylim(ylim_min, ylim_max)
ax2.set_ylim(ylim_min, ylim_max)
ax2.set_xlim(0, 100)
ax1.set_xlim(0, end_value+500)

# 绘点区
ax2.text(52, 275, 'l')
ax2.text(4, 191, 'α')
ax2.text(49, 145, 'α+β')
ax2.text(32, 200, 'α+l')
ax2.text(84, 194, 'β+l')
ax2.text(98, 180, 'β')

# 设置两个子图的x轴和y轴刻度相同
ax3 = ax2.twinx()
ax3.set_ylim(ylim_min, ylim_max + 0.5, 10)
ax2.set_yticklabels([])  # 不显示左轴刻度
yticks = np.arange(ylim_min, ylim_max + 0.5, 10)  # y轴的分度
ax1.set_yticks(yticks)
ax2.set_yticks(yticks)
ax2.grid(True)
plt.subplots_adjust(wspace=-0.01)  # 调整子图之间的宽度和高度间距
ax3.set_yticks(yticks)

# 画横虚线
ax1.plot(x_pb_pingtai, y_pb_pingtai, linestyle='dashed', color='red')
ax1.plot(x_30_guaidian, y_30_guaidian, linestyle='dashed', color='red')
ax1.plot(x_619_pingtai, y_619_pingtai, linestyle='dashed', color='red')
ax1.plot(x_80_guaidian, y_80_guaidian, linestyle='dashed', color='red')
ax1.plot(x_sn_pingtai, y_sn_pingtai, linestyle='dashed', color='red')
ax2.plot(x_30_ax2_guaidain, y_30_ax2_guaidain, linestyle='dashed', color='red')
ax2.plot(x_619_ax2_pingtai, y_619_ax2_pingtai, linestyle='dashed', color='red')
ax2.plot(x_80_ax2_guaidain, y_80_ax2_guaidain, linestyle='dashed', color='red')
ax2.plot(x_sn_ax2_pingtai, y_sn_ax2_pingtai, linestyle='dashed', color='red')

# 画斜虚线
x_1 = [b1, 19.7]
y_1 = [a1, a3]
x_2 = [19.7, 0]
y_2 = [a3, 0]
x_3 = [b5, 97.3]
y_3 = [a5, a3]
x_4 = [97.3, b5]
y_4 = [a3, 110]
ax2.plot(x_1, y_1, linestyle='dashed', color='black')
ax2.plot(x_2, y_2, linestyle='dashed', color='black')
ax2.plot(x_3, y_3, linestyle='dashed', color='black')
ax2.plot(x_4, y_4, linestyle='dashed', color='black')

# 画竖虚线
x_6 = [30, 30]
y_6 = [a2, 0]
x_7 = [80, 80]
y_7 = [a4, 0]
x_8 = [61.9, 61.9]
y_8 = [a3, 0]
ax2.plot(x_6, y_6, linestyle='dashed', color='red')
ax2.plot(x_7, y_7, linestyle='dashed', color='red')
ax2.plot(x_8, y_8, linestyle='dashed', color='red')
'''
y_xiangdian=[a1,a2,a3,a4,a5]
x_xiangdian=[b1,b2,b3,b4,b5]
for i in range(len([a1,a2,a3,a4,a5])):
    plt.text(x_xiangdian[i], y_xiangdian[i], f'({x_xiangdian[i]},{y_xiangdian[i]})')
'''
'''
x_ticks = [0, 20,30, 40, 60, 61.9,80, 100]  # 你想要显示的x轴刻度位置
x_ticklabels = ['0', '20', '30','40', '60', '61.9','80', '100']  # 与刻度位置对应的标签
ax2.set_xticks(x_ticks)
ax2.set_xticklabels(x_ticklabels)  
'''
# 显示图像
plt.show()
