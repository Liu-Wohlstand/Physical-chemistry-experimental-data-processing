"""替换示例数据及默认常数即可"""
import numpy as np

'''示例数据
Ea = np.array([0.34940, 0.34941, 0.34952])
Eb = np.array([0.46120, 0.46113, 0.46103])
Ec = np.array([0.38460, 0.38445, 0.38438])
示例数据
Ea = np.array([0.34672,0.34636,0.34631])
Eb = np.array([0.46070,0.46072,0.46072])
Ec = np.array([0.38093,0.38095,0.38080])
示例数据
Ea = np.array([0.34118,0.34112,0.34124])
Eb = np.array([0.45978,0.45972,0.45965])
Ec = np.array([0.37791,0.37779,0.37769])
'''
Ea = np.array([0.32781])
Eb = np.array([0.46471])
Ec = np.array([0.38771])
Ea_mean = np.mean(Ea)
Eb_mean = np.mean(Eb)
Ec_mean = np.mean(Ec)
print(f'Ea平均值为{Ea_mean},Eb平均值为 {Eb_mean},Ec平均值为{Ec_mean}')
t = 15.3  # 输入温度，以摄氏度计
T = t + 273.15
Eqhq = 0.6993 - 0.00074 * (t - 25)  # 请输入醌氢醌电极电极电动势
Ehg = 0.2410 - 0.00076 * (t - 25)  # 请输入甘汞电极电极电动势
print(f'醌氢醌电极电势为{Eqhq}V，甘汞电极电极电动势为{Ehg}V')
c1 = 0.02  # 输入硝酸银溶液中银离子的摩尔浓度
c2 = 0.02  # 输入氯化钾中氯离子的摩尔浓度
ph = (Eqhq - Ehg - Ea_mean) / (0.000198 * T)
print('HCl溶液ph值为：', ph)
Eag = Eb_mean + Ehg
print(f'E Ag/Ag+={Eag}V')
Ksp = (c1 * c2 * 0.86 ** 2) / (10 ** (Ec_mean / (0.000198 * T)))
print('Ksp=', Ksp)
