import matplotlib.pyplot as plt
import numpy as np
n = 1000
x= np.random.normal(0,1,n)
xx= np.random.uniform(-4,4,(1,n))
y= np.random.normal(0,1,n)
yy= np.random.uniform(-4,4,(1,n))
plt.scatter(x,y,color='b',marker =',',label = '正态分布')
plt.scatter(xx,yy,color='y',marker ='o',label = '均匀分布')
plt.legend(1)
plt.title('标准正态分布',fontsize = 20)
plt.text(2.5,2.5,"均值: \n标准差: 1")
plt.xlim(-4,4)
plt.ylim(-4,4)
plt.xlabel('横坐标x',fontsize = 14)
plt.ylabel('纵坐标y',fontsize = 14)
plt.show()


