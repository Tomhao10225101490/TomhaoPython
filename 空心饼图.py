import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(16, 9), dpi=80)
data=np.random.randint(1,50,8)
print(data)
labels=np.array(["China","日本人民","美国","America","e","f","g","h"])
plt.pie(data,autopct="%3.1f%%",radius=1,pctdistance=1.2,wedgeprops={"width":0.8})
plt.legend(labels)
plt.show()
