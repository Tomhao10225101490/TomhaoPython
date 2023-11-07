import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
# 读取附件2中的销售流水明细数据
sales_data = pd.read_excel('附件2_副本.xlsx')

# 分析蔬菜各品类的销售量分布规律
category_counts = sales_data['单品编码'].value_counts()
category_counts.plot(kind='bar')
plt.title('蔬菜品类销售量分布')
plt.xlabel('蔬菜品类')
plt.ylabel('销售量')
plt.show()

# 分析蔬菜各单品的销售量分布规律
item_counts = sales_data['Item'].value_counts()
item_counts.plot(kind='bar')
plt.title('蔬菜单品销售量分布')
plt.xlabel('蔬菜单品')
plt.ylabel('销售量')
plt.show()

# 分析蔬菜品类和单品之间的关联关系
item_category_data = sales_data[['单品编码', 'Item']].drop_duplicates()
item_category_counts = item_category_data.groupby(['Category', 'Item']).size().reset_index(name='counts')
item_category_counts.head()