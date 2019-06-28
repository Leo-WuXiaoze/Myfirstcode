import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 加载数据
# df = sns.load_dataset("tips")
# print(df,type(df))
# df.to_csv(path_or_buf="../data/tips2",index=True,index_label='row_id')
df = pd.read_csv("../data/tips.csv")
df.info()
df.head()
print('性别与小费金额是否存在相关性')
female_mean = df[df['sex'] == "Female"]['tip'].mean()
male = df[df['sex'] == "Male"]["tip"]
male_mean = df[df['sex'] == "male"]['tip'].mean()

