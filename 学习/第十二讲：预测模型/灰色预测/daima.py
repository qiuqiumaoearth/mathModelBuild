'''
GM(1,1)模型代码的写作思路
1.画出原始数据的实践序列图，判断原始数据中是否有负数或低于四期，是，则报错，否进行下一步
2.对一次累加后的数据进行准指数规律检验，返回两个指标
    指标1 光滑比小于0.5的数据占比
    指标2 除去前两个时期外，光滑比
'''




# # -*- coding: utf-8 -*-
# """
# Spyder Editor

# This is a temporary script file.
# """
import numpy as np
import math

history_data = [724.57,746.62,778.27,800.8,827.75,871.1,912.37,954.28,995.01,1037.2]
n = len(history_data)
X0 = np.array(history_data)

#累加生成
history_data_agg = [sum(history_data[0:i+1]) for i in range(n)]
X1 = np.array(history_data_agg)#累加x1

#计算数据矩阵B和数据向量Y
B = np.zeros([n-1,2])
Y = np.zeros([n-1,1])
for i in range(0,n-1):
    B[i][0] = -0.5*(X1[i] + X1[i+1])
    B[i][1] = 1
    Y[i][0] = X0[i+1]

#计算GM(1,1)微分方程的参数a和u
#A = np.zeros([2,1])
A = np.linalg.inv(B.T.dot(B)).dot(B.T).dot(Y)
a = A[0][0]
u = A[1][0]

#建立灰色预测模型
XX0 = np.zeros(n)
XX0[0] = X0[0]
for i in range(1,n):
    XX0[i] = (X0[0] - u/a)*(1-math.exp(a))*math.exp(-a*(i));


#模型精度的后验差检验
e = 0      #求残差平均值
for i in range(0,n):
    e += (X0[i] - XX0[i])
e /= n
print("残差平均值：",e)

#求历史数据平均值
aver = 0;     
for i in range(0,n):
    aver += X0[i]
aver /= n

#求历史数据方差
s12 = 0;     
for i in range(0,n):
    s12 += (X0[i]-aver)**2;
s12 /= n

#求残差方差
s22 = 0;       
for i in range(0,n):
    s22 += ((X0[i] - XX0[i]) - e)**2;
s22 /= n

#求后验差比值
C = s22 / s12   

#求小误差概率
cout = 0
for i in range(0,n):
    if abs((X0[i] - XX0[i]) - e) < 0.6754*math.sqrt(s12):
        cout = cout+1
    else:
        cout = cout
P = cout / n

if (C < 0.35 and P > 0.95):
    #预测精度为一级
    m = 10   #请输入需要预测的年数
    print('往后m各年负荷为：')
    f = np.zeros(m)
    for i in range(0,m):
        f[i] = (X0[0] - u/a)*(1-math.exp(a))*math.exp(-a*(i+n))    
else:
    print('灰色预测法不适用')



# # 关于出现图案里面的中文不显示，只有口口的样子
# # 解决方案：

# import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置字体为宋体或其他中文字体
# plt.figure(figsize=(8, 4))
# plt.plot([1, 2, 3, 4, 5], [10, 12, 5, 8, 9], 'b-o')
# plt.xlabel('X轴')
# plt.ylabel('Y轴')
# plt.title('中文标题')
# plt.grid(True)
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# # 创建一个圆的坐标点
# theta = np.linspace(0, 2 * np.pi, 100)  # 创建角度范围从0到2*pi
# r = 1.0  # 圆的半径

# # 计算圆上的点的坐标
# x = r * np.cos(theta)
# y = r * np.sin(theta)

# # 创建坐标图
# plt.figure(figsize=(6, 6))  # 设置图形大小
# plt.plot(x, y, label='圆', color='b')  # 绘制圆
# plt.xlabel('X轴')  # 设置X轴标签
# plt.ylabel('Y轴')  # 设置Y轴标签
# plt.title('圆的坐标图')  # 设置标题
# plt.legend()  # 显示图例
# plt.grid(True)  # 显示网格

# # 显示图形
# plt.show()


# '''输入原始数据并做出时间序列图'''
# import pandas as pd
# import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimSun']

# # 导入CSV文件到DataFrame
# df = pd.read_csv('daima.csv',encoding='utf-8')

# # 将日期列解析为日期时间格式
# #df['Date'] = pd.to_datetime(df['Date']) #将文件中的Date列解析为日期时间格式

# # 设置日期列作为索引（如果未设置的话）
# # df.set_index('Date', inplace=True)

# # 创建时间序列图
# plt.figure(figsize=(12, 6))# 图形窗口的大小
# plt.plot(df['year'], df['zong'], label='时间序列数据', color='blue')
# #创建一个二维图表，第一个"date"作为x轴，第二个“Value”作为y轴，图例标签为“时间序列数据”，颜色为蓝色
# plt.xlabel('时间')
# plt.ylabel('值')
# plt.title('时间序列图')
# plt.legend()


# plt.grid(True)

# # 显示图像
# plt.show()


# #读取第几行数据
# import pandas as pd

# # 读取CSV文件
# df = pd.read_csv('daima.csv',encoding='utf-8')

# # 打印 DataFrame 的前几行
# print(df.head(1))


'''读取xlsx 文件进行处理成为csv文件
# import pandas as pd

# # 读取Excel文件
# excel_file = 'daima.xlsx'  # 替换为您的Excel文件路径
# df = pd.read_excel(excel_file)

# # 将数据保存为CSV文件
# csv_file = 'daima.csv'  # 指定CSV文件路径
# df.to_csv(csv_file, index=False)  # index=False 表示不保存索引列
'''


















