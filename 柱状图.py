import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams["axes.unicode_minus"] = False
y1 = np.random.randint(10,100,10)
y2 = np.random.randint(-100,-10,13)
plt.bar(range(len(y1)), y1, width=0.8, facecolor='g',edgecolor='w',label = '统计量1')
plt.bar(range(len(y2)), y2, width=0.8, facecolor='r',edgecolor='k',label = '统计量2')

plt.title('柱状图',fontsize = 20)

plt.legend()
plt.show()