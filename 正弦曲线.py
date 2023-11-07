import matplotlib.pyplot as plt
import numpy as np
 
x = np.linspace(0, 10, 100)
y = np.sin(x)
 
# 创建一个图形窗口
plt.figure(figsize=(8,6))
 
# 绘制折线图
plt.plot(x, y)
 
# 设置坐标轴标签和标题
plt.xlabel('x')
plt.ylabel('y')
plt.title('正弦曲线')
 
# 显示图形
plt.show()
