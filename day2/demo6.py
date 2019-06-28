import pandas as pd
import numpy as np
import seaborn as sns

# 加载数据
# df = sns.load_dataset("tips")
# print(df,type(df))
# df.to_csv(path_or_buf="../data/tips2",index=True,index_label='row_id')
df = pd.read_csv("../data/tips.csv")
df.info()
df.head()
print('消费金额与消费总额是否存在相关性')
# 散点图
total_bill = df['total_bill']
tip = df['tip']
import matplotlib.pyplot as plt


# 指定x y轴
plt.scatter(total_bill, tip)
plt.rcParams['font.sans-serif']=['SimHei']
plt.xlabel('tool_bill')
plt.ylabel('tip')
plt.title("总金额与小费相关的散点图")
plt.show()
