import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 获取数据
df = pd.read_csv("../data/house.csv")
df.info()
print('-' * 30)
# print(df.head(n=3))
# print('-'*30)
# 数据清理
# 特征工程  axis =0 代表行 axis=1 代表列
y_true = df['price'] + 10  # 期望值
X = df.drop(["price", "row_id"], axis=1)
print("期望的价格：\n", y_true)
print('-' * 30)
print("面积特征）:\n", X)
print('-' * 30)
# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y_true, test_size=0.2, random_state=3)
print("测试集的数据：\n", X_test, "\n", y_test)
print('-' * 30)
print('训练集的的数据：\n', X_train, "\n", y_train)

print('-' * 30)
lr = LinearRegression()
# 训练模型：把训练集的特征值和目标值交给模型(有目标值就是有监督的机器学习)
# LinearRegression线性回归模型
lr.fit(X_train, y_train, 2)
# gg=lr.fit(X_train,y_train,0)
# # print(type(gg))
# 训练的过程就是找权重的过程
print(lr.intercept_)

print('获取模型训练的权重', lr.coef_)
# 通过测试集验证模型,返回的是预测值
y_predict = lr.predict(X_test)
print(y_predict, "\n", X_test)
# 根据均方误差求误差值

# print(y_predict.shape)
print('均方误差为:', mean_squared_error(y_test, y_predict))
