a = []
b = []
c = []
import math
for i in range(1,9):
 t=float(input("请输入第{}组摄氏度数据：".format(i)))
 T=t=273.15+t
 y=1/T*1000
 p=float(input("请输入第{}组压强数据：".format(i)))
 lnp=math.log(p)
 print('T=',T)
 print('1/T=',y)
 print('lnp=',lnp)
 a.append(T)
 b.append(y)
 c.append(lnp)
print('T',a)
print('1/T*1000:',b)
print('lnp:',c)