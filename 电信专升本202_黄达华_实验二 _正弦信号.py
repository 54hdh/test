import matplotlib.pyplot as plt
import numpy as np
#   linspace 第一个参数序列起始值，第二个参数序列结束值，第三个参数为样本数默认50
x = np.linspace(0,3*np.pi,100)#从0开始到3pai，总共100个点
y = np.sin(x)#设置函数y是一个参数为x的正弦函数

plt.rcParams['font.sans-serif']=['SimHei']#加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False#用来显示正常负号
plt.subplot(1,2,1)#总共一行两列，在第一行第一列操作
plt.title(r'$f(x)=sin(x)$')#显示y=sin（x）这个标题
plt.plot(x,y)#显示连续函数y的点
#plt.show()
x1 = [t*0.375*np.pi for t in x]#将3/8pi*t赋给x1，其中t的取值范围为x的取值范围
y1 = np.sin(x1)#设置y1为以x1为参数的正弦函数
plt.subplot(1,2,2)#总共一行两列，在第一行第二列操作
plt.title(r'$f(x)=sin(\omega),\omega = \frac{3}{8} \pi$')#显示标题
plt.plot(x,y1)#显示连续函数y1的点
plt.show()#显示图像