import pandas as pd  
import numpy as np  
from pulp import LpMaximize, LpProblem, LpVariable, lpSum  
import statsmodels.api as sm  
  
# 读取数据  
data = pd.read_excel("合并后的数据.xlsx")  
  
# 提取销售数据  
sales_data = data[['销售日期', '单品编码', '销量(千克)', '销售单价(元/千克)', '批发价格(元/千克)', '损耗率(%)', '单品名称', '分类名称']]  
  
# 筛选出销售时间在2023年6月24日至30日的数据  
sales_data = sales_data[(sales_data['销售日期'] >= '2023-06-24') & (sales_data['销售日期'] <= '2023-06-30')]  
  
# 筛选出可售品种的信息  
可售品种 = sales_data[sales_data['销量(千克)'] > 0]  
  
# 构建时间序列模型来预测2023年7月1日的市场需求（以每个可售品种为单位）  
市场需求预测 = {}  
for 单品编码, group in 可售品种.groupby('单品编码'):  
    # 创建时间序列数据  
    时间序列数据 = group.groupby('销售日期')['销量(千克)'].sum()  
      
    # 使用时间序列模型进行预测（这里使用ARIMA模型示例，您可以根据数据特点选择合适的模型）  
    模型 = sm.tsa.ARIMA(时间序列数据, order=(1, 1, 1))  
    模型_fit = 模型.fit()  
    预测结果 = 模型_fit.forecast(steps=1)  # 预测2023年7月1日的销量  
      
    市场需求预测[单品编码] = 预测结果[0]  
  
# 构建优化模型  
model = LpProblem(name="蔬菜补货和定价问题", sense=LpMaximize)  
  
# 创建变量  
补货量 = {}  
定价 = {}  
for 单品编码, row in 可售品种.iterrows():  
    补货量[单品编码] = LpVariable(name=f"补货量_{单品编码}", lowBound=row['最小陈列量'], upBound=None, cat='Continuous')  
    定价[单品编码] = LpVariable(name=f"定价_{单品编码}", lowBound=0, upBound=None, cat='Continuous')  
  
# 定义目标函数  
总收益 = lpSum((补货量[单品编码] * 定价[单品编码] * 市场需求预测[单品编码]) -   
              (补货量[单品编码] * row['批发价格(元/千克)'] +   
               补货量[单品编码] * 市场需求预测[单品编码] * row['损耗率(%)'] * row['销售单价(元/千克)'])   
              for 单品编码, row in 可售品种.iterrows())  
  
model += 总收益  
  
# 添加约束条件  
model += lpSum(补货量.values()) >= 27  
model += lpSum(补货量.values()) <= 33  
  
# 添加约束条件：总销量等于总补货量  
for 单品编码, row in 可售品种.iterrows():  
    model += lpSum(补货量[单品编码]) == row['销量(千克)']  
  
# 求解问题  
model.solve()  
  
# 打印结果  
print("优化结果：")  
for 单品编码 in 补货量.keys():  
    print(f"单品编码: {单品编码}, 补货量: {补货量[单品编码].varValue}, 定价: {定价[单品编码].varValue}")  
  
# 输出最优总收益  
print(f"最优总收益: {model.objective.value()}")